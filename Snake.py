from random import randint

import pygame

# Константы для размеров поля и сетки.
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения.
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвета.
BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки.
SPEED = 20

# Настройка игрового окна.
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32
)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс игровых объектов."""

    def __init__(self) -> None:
        """Инициализирует позицию и цвет объекта."""
        self.position = (
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2
        )
        self.body_color = None

    def draw(self):
        """Отрисовывает игровой объект."""
        pass


class Apple(GameObject):
    """Класс, описывающий яблоко."""

    def __init__(self):
        """Создаёт яблоко и задаёт его цвет и позицию."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self, snake=None):
        """Размещает яблоко в случайной свободной клетке."""
        while True:
            self.position = (
                randint(0, GRID_WIDTH - 1) * GRID_SIZE,
                randint(0, GRID_HEIGHT - 1) * GRID_SIZE
            )

            if snake is None or self.position not in snake.positions:
                break

    def draw(self):
        """Отрисовывает яблоко."""
        rect = pygame.Rect(
            self.position, (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку."""

    def __init__(self):
        """Создаёт змейку и задаёт её начальные параметры."""
        super().__init__()
        self.body_color = SNAKE_COLOR
        self.direction = RIGHT
        self.next_direction = None
        self.length = 1
        self.positions = [self.position]
        self.last = None

    def draw(self):
        """Отрисовывает змейку на игровом поле."""
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки.
        head_rect = pygame.Rect(
            self.positions[0], (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента.
        if self.last:
            last_rect = pygame.Rect(
                self.last, (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(
                screen, BOARD_BACKGROUND_COLOR, last_rect
            )

    def get_head_position(self):
        """Возвращает координаты головы змейки."""
        return self.positions[0]

    def move(self):
        """Перемещает змейку на одну клетку."""
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction

        new_head = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        )

        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.last = self.positions.pop(-1)
        else:
            self.last = None

    def reset(self):
        """Возвращает змейку в начальное состояние."""
        self.next_direction = None
        self.length = 1
        self.positions = [self.position]
        self.last = None
        self.direction = RIGHT

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None


def handle_keys(game_object):
    """Обрабатывает нажатия клавиш управления."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.KEYDOWN:
            if (
                event.key == pygame.K_UP
                and game_object.direction != DOWN
            ):
                game_object.next_direction = UP

            elif (
                event.key == pygame.K_DOWN
                and game_object.direction != UP
            ):
                game_object.next_direction = DOWN

            elif (
                event.key == pygame.K_LEFT
                and game_object.direction != RIGHT
            ):
                game_object.next_direction = LEFT

            elif (
                event.key == pygame.K_RIGHT
                and game_object.direction != LEFT
            ):
                game_object.next_direction = RIGHT


def main():
    """Запускает игру."""
    pygame.init()

    apple = Apple()
    snake = Snake()

    # Перегенерируем яблоко, если оно попало на змейку.
    apple.randomize_position(snake)

    # Первоначальная очистка игрового поля.
    screen.fill(BOARD_BACKGROUND_COLOR)

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.update_direction()
        snake.move()

        # Проверяем поедание яблока.
        if apple.position == snake.get_head_position():
            snake.length += 1
            apple.randomize_position(snake)

        # Проверяем столкновение змейки с собой.
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()
            screen.fill(BOARD_BACKGROUND_COLOR)
            apple.draw()
            snake.draw()

        # Отрисовка.
        apple.draw()
        snake.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()
