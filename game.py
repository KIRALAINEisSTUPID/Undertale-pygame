import pygame
import sys
import funcs
from funcs import Player
from pygame import mixer
pygame.init()

# Параметры окна
width, height = 1450, 900
screen = pygame.display.set_mode((width, height))
logo = pygame.image.load("Assets/img/icons/soul.png")
bg_image = pygame.image.load("Assets/img/backgrounds/undertale-game.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Undertale")

# Инициализация игрока
player = Player(400, 500)
clock = pygame.time.Clock()

# Группа спрайтов
all_sprites = pygame.sprite.Group(player)

pygame.mixer.init()
try:
    pygame.mixer.music.load("Assets/sounds/soundtracks/OneShot OST - Thanks For Everything.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
except pygame.error:
    print("Music file not found!")
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
    clock.tick(45)
   
    # Обновление спрайтов
    all_sprites.update()

pygame.quit()
sys.exit()
