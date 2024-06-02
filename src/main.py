import pygame
from os.path import isfile
from configparser import ConfigParser

def load_configuration() -> ConfigParser:
    configuration = ConfigParser()
    configuration["RESOLUTION"] = {
        "WIDTH":  "800",
        "HEIGHT": "600",
    }

    configuration_file_path = "./Config/configuration.ini"

    if isfile(configuration_file_path):
        _ = configuration.read(configuration_file_path)
    else:
        with open("./Config/configuration.ini", "x") as file:
            configuration.write(file)

    return configuration

def main() -> None:
    configuration = load_configuration()

    resolution = configuration["RESOLUTION"]
    witdh      = resolution.getint("WIDTH")
    height     = resolution.getint("HEIGHT")


    _ = pygame.init()
    screen = pygame.display.set_mode((witdh, height))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game Loop!


        _ = screen.fill("purple")
        pygame.display.flip()
        _ = clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
