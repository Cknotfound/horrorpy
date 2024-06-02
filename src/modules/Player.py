from pygame.math import Vector2

class Player:
    def __init__(self, position: Vector2):
        self.position = position or Vector2(0, 0)
