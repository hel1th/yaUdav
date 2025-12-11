
import random
import pygame

from constants import (
    APPLE_COLOR,
    GRID_HEIGHT,
    GRID_SIZE,
    GRID_WIDTH,
)
from game_object import GameObject


class Apple(GameObject):
    """Яблоко на игровой карте."""

    def __init__(self):
        super().__init__(APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self):
        """Выбирает новую случайную позицию."""
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    def draw(self, surface):
        """Рисует яблоко."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, rect)
