from pygame.math    import Vector2
from modules.Player import Player

def main() -> None:
    new_player = Player(Vector2(0, 0))
    print(new_player.position)

if __name__ == "__main__":
    main()

