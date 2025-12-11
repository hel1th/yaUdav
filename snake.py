import random

import pygame

from constants import (
    BOARD_BACKGROUND_COLOR,
    GRID_SIZE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_COLOR,
)
from game_object import GameObject


class Snake(GameObject):
    """Змейка и её логика."""

    def __init__(self):
        super().__init__(SNAKE_COLOR)
        self.length = 1
        self.positions = [self.position]
        self.direction = (GRID_SIZE, 0)
        self.next_direction = None
        self.last = None

    def get_head_position(self):
        """Возвращает позицию головы."""
        return self.positions[0]

    def update_direction(self):
        """Обновляет направление с запретом разворота назад."""
        if self.next_direction is None:
            return

        dx, dy = self.direction
        ndx, ndy = self.next_direction

        if (ndx, ndy) != (-dx, -dy):
            self.direction = self.next_direction

        self.next_direction = None

    def move(self):
        """Перемещает змейку + проверяет столкновение."""
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction

        new_head = (
            (head_x + dx) % SCREEN_WIDTH,
            (head_y + dy) % SCREEN_HEIGHT,
        )

        if new_head in self.positions[1:]:
            self.reset()
            return

        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self, surface):
        """Рисует змейку и стирает хвост."""
        if self.last:
            rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, rect)

        for pos in self.positions:
            rect = pygame.Rect(pos, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.body_color, rect)

    def reset(self):
        """Полный сброс змейки."""
        self.length = 1
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.positions = [self.position]
        self.next_direction = None
        self.last = None

        self.direction = random.choice([
            (GRID_SIZE, 0),
            (-GRID_SIZE, 0),
            (0, GRID_SIZE),
            (0, -GRID_SIZE),
        ])
