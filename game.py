import pygame
import sys

# Инициализация Pygame
pygame.init()

# Задаем размеры окна
width, height = 1450, 900
screen = pygame.display.set_mode((width, height))

# Задаем заголовок окна
pygame.display.set_caption("Мое окно в Pygame")

# Основной цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона цветом (например, белый)
    screen.fill((255, 255, 255))

    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
