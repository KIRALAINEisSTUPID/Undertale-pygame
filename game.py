import pygame
import sys

pygame.init()

width, height = 1450, 900
screen = pygame.display.set_mode((width, height))
logo = pygame.image.load("Assets/img/icons/soul.png")
bg_image = pygame.image.load("Assets/img/backgrounds/undertale-game.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Undertale")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_image, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
