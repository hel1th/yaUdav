import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class GameObject:
    """Базовый класс для всех игровых объектов."""

    def __init__(self, color):
        """
        :param color: RGB-цвет объекта.
        """
        self.body_color = color
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw(self, surface):
        """Абстрактный метод — должен быть переопределён."""
        pass
