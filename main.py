from constants import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        screen.fill((0,0,0))
        pygame.display.flip()

    print(
        f"""
        Starting asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}""")

if __name__ == "__main__":
    main()