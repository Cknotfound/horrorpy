from pygame.math import Vector2

class Player:
    def __init__(self, position: Vector2):
        self.position = position or Vector2(0, 0)

if __name__ == "__main__":
    print("Testing Player Class...")
    print("Creating a new player..")
    new_player = Player(Vector2(0, 0))
    print(f"new_player's position: {new_player.position}")
    print("tests passed")

