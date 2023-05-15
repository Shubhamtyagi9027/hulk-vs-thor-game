import pygame, random
from Constants import *
pygame.mixer.pre_init(44100,16,2,512)
pygame.init()

SCREEN = pygame.display.set_mode(SIZE)

sprite_group = pygame.sprite.Group()
pygame.mixer.music.load("Thor music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def main():
    bgImage = pygame.image.load("bg.jpeg")

    clock = pygame.time.Clock()
    FPS = 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.blit(bgImage, (0, 0))

        sprite_group.draw(SCREEN)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(FPS)

main()