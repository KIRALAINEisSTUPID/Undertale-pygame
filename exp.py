import pygame

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Загрузка спрайтов
sprites = {
    'down': [pygame.image.load('down_1.png'), pygame.image.load('down_2.png')],
    'up': [pygame.image.load('up_1.png'), pygame.image.load('up_2.png')],
    'left': [pygame.image.load('left_1.png'), pygame.image.load('left_2.png')],
    'right': [pygame.image.load('right_1.png'), pygame.image.load('right_2.png')]
}

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = sprites
        self.image = self.images['down'][0]  # Начальный спрайт
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 'down'
        self.current_frame = 0
        self.frame_delay = 10  # задержка между кадрами анимации
        self.frame_counter = 0

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Перемещение и смена направления
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            self.direction = 'right'
        elif keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
            self.direction = 'up'
        elif keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
            self.direction = 'down'

        # Обновление анимации
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.images[self.direction])
            self.image = self.images[self.direction][self.current_frame]
            self.frame_counter = 0

# Создание игрока
player = Player(400, 300)
all_sprites = pygame.sprite.Group(player)

# Основной цикл игры
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Отрисовка
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(30)

pygame.quit()
