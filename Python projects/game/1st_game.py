import pygame

import os

MAIN_SPRITE = pygame.image.load(os.path.join("game", "mario.png"))

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Harry's Game")

WHITE = (255, 255, 255)

FPS = 60

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(MAIN_SPRITE, (0, 0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()