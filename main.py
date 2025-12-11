
import pygame

from apple import Apple
from constants import BOARD_BACKGROUND_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH
from snake import Snake


def handle_keys(snake):
    """Обрабатывает ввод пользователя."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.next_direction = (0, -20)
            elif event.key == pygame.K_DOWN:
                snake.next_direction = (0, 20)
            elif event.key == pygame.K_LEFT:
                snake.next_direction = (-20, 0)
            elif event.key == pygame.K_RIGHT:
                snake.next_direction = (20, 0)


def main():
    """Главный цикл игры."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Изгиб Питона')

    snake = Snake()
    apple = Apple()
    clock = pygame.time.Clock()

    screen.fill(BOARD_BACKGROUND_COLOR)
    pygame.display.update()

    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()
        clock.tick(20)


if __name__ == '__main__':
    main()
