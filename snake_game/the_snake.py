from random import choice, randint
import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
CENTER_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета:
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 15

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

class gameObject:
    """Класс игрового объекта"""
    def __init__(self, position=None):
        self.position = position if position else CENTER_POSITION
        self.bodyColor = None
    
    def draw(self):
        raise NotImplementedError("Метод draw() должен быть реализован в подклассе")

class Apple(gameObject):
    """Класс яблока"""
    def __init__(self):
        super().__init__()
        self.bodyColor = APPLE_COLOR
        self.randomizePosition()
    
    def randomizePosition(self):
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )
    
    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.bodyColor, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

class Snake(gameObject):
    """Класс змейки"""
    def __init__(self):
        super().__init__()
        self.bodyColor = SNAKE_COLOR
        self.record_length = 1  # Рекордная длина
        self.reset()
    
    def reset(self):
        self.positions = [self.position]
        self.length = 1
        self.direction = RIGHT
        self.nextDirection = None
        self.last = None
        self.updateTitle()  # Обновляем заголовок при сбросе
    
    def updateTitle(self):
        if self.length > self.record_length:
            self.record_length = self.length
        pygame.display.set_caption(
            f'Змейка | Длина: {self.length} | Рекорд: {self.record_length}'
        )
    
    def updateDirection(self):
        if self.nextDirection:
            self.direction = self.nextDirection
            self.nextDirection = None
    
    def move(self):
        self.updateDirection()
        head_x, head_y = self.getHeadPosition()
        dir_x, dir_y = self.direction
        new_x = (head_x + dir_x * GRID_SIZE) % SCREEN_WIDTH
        new_y = (head_y + dir_y * GRID_SIZE) % SCREEN_HEIGHT
        new_position = (new_x, new_y)
        
        self.last = self.positions[-1] if len(self.positions) > 1 else None
        self.positions.insert(0, new_position)
        
        if len(self.positions) > self.length:
            self.positions.pop()
    
    def getHeadPosition(self):
        return self.positions[0]
    
    def draw(self):
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.bodyColor, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        
        if self.last and len(self.positions) <= self.length:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

def handleKeys(gameObject):
    """Метод считывания сигналов клавиш"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
            if event.key == pygame.K_UP and gameObject.direction != DOWN:
                gameObject.nextDirection = UP
            elif event.key == pygame.K_DOWN and gameObject.direction != UP:
                gameObject.nextDirection = DOWN
            elif event.key == pygame.K_LEFT and gameObject.direction != RIGHT:
                gameObject.nextDirection = LEFT
            elif event.key == pygame.K_RIGHT and gameObject.direction != LEFT:
                gameObject.nextDirection = RIGHT

def main():
    pygame.init()
    
    snake = Snake()
    apple = Apple()
    
    while True:
        clock.tick(SPEED)
        
        handleKeys(snake)
        snake.move()
        
        # Проверка на съедение яблока
        if snake.getHeadPosition() == apple.position:
            snake.length += 1
            snake.updateTitle()  # Обновляем заголовок при увеличении длины
            apple.randomizePosition()
            while apple.position in snake.positions:
                apple.randomizePosition()
        
        # Проверка на столкновение с собой
        if len(snake.positions) > 4 and snake.getHeadPosition() in snake.positions[1:]:
            snake.reset()
        
        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()