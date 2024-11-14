import pygame
import sys
import funcs
from funcs import Player

pygame.init()

# Параметры окна
width, height = 1450, 900
screen = pygame.display.set_mode((width, height))
logo = pygame.image.load("Assets/img/icons/soul.png")
bg_image = pygame.image.load("Assets/img/backgrounds/undertale-game.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Undertale")

# Инициализация игрока
player = Player(400, 300)
clock = pygame.time.Clock()

# Группа спрайтов
all_sprites = pygame.sprite.Group(player)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисуем фон
    screen.blit(bg_image, (0, 0))

    # Отрисовка всех спрайтов
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.update()

    # Ограничение FPS
    clock.tick(30)
   
    # Обновление спрайтов
    all_sprites.update()

pygame.quit()
sys.exit()
