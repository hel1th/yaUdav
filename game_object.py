
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class GameObject:
    """Базовый игровой объект."""

    def __init__(self, color):
        """Создаёт объект с указанным цветом."""
        self.body_color = color
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def draw(self, surface):
        """Абстрактный метод — должен быть переопределён."""
        raise NotImplementedError
