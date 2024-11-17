import subprocess
import platform
import os
import pygame
def open_terminal(command):
    system = platform.system()

    if system == "Linux":
        try:
            # Запуск команды с nohup в фоновом режиме
            subprocess.Popen(['nohup', 'kitty', '-e', 'fish', '-c', command, '&'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            subprocess.Popen(['nohup', 'gnome-terminal', '--', 'bash', '-c', command, '&'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif system == "Darwin":  # macOS
        # Используем osascript для выполнения команды без открытия окна
        subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "{command}"'])
    elif system == "Windows":
        # Используем start для минимизации окна
        subprocess.Popen(['start', 'cmd', '/c', f"start /min {command}"], shell=True)



PLAYER_SPEED = 5
SPRITE_SCALE = 3  # Коэффициент увеличения спрайта

# Загрузка и масштабирование спрайтов
def load_and_scale_sprite(path):
    image = pygame.image.load(path)
    scaled_image = pygame.transform.scale(image, (image.get_width() * SPRITE_SCALE, image.get_height() * SPRITE_SCALE))
    return scaled_image

sprites = {
    'down': [load_and_scale_sprite('Assets/img/sprites/Frisk/Down/0.png'),
             load_and_scale_sprite('Assets/img/sprites/Frisk/Down/1.png'),
             load_and_scale_sprite('Assets/img/sprites/Frisk/Down/2.png'),
             load_and_scale_sprite('Assets/img/sprites/Frisk/Down/3.png')],
    'up': [load_and_scale_sprite('Assets/img/sprites/Frisk/Up/0.png'),
           load_and_scale_sprite('Assets/img/sprites/Frisk/Up/1.png'),
           load_and_scale_sprite('Assets/img/sprites/Frisk/Up/2.png'),
           load_and_scale_sprite('Assets/img/sprites/Frisk/Up/3.png')],
    'left': [load_and_scale_sprite('Assets/img/sprites/Frisk/Left/0.png'),
             load_and_scale_sprite('Assets/img/sprites/Frisk/Left/1.png')],
    'right': [load_and_scale_sprite('Assets/img/sprites/Frisk/Right/0.png'),
              load_and_scale_sprite('Assets/img/sprites/Frisk/Right/1.png')]
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
        self.frame_delay = 10  # Задержка между кадрами анимации
        self.frame_counter = 0

    def update(self):
        keys = pygame.key.get_pressed()
        moving = False
        new_direction = self.direction

        # Перемещение и смена направления
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED
            new_direction = 'left'
            moving = True
        elif keys[pygame.K_RIGHT] and self.rect.x < 1400:
            self.rect.x += PLAYER_SPEED
            new_direction = 'right'
            moving = True
        elif keys[pygame.K_UP] and self.rect.y > 500:
            self.rect.y -= PLAYER_SPEED
            new_direction = 'up'
            moving = True
        elif keys[pygame.K_DOWN] and self.rect.y < 800:
            self.rect.y += PLAYER_SPEED
            new_direction = 'down'
            moving = True

        elif keys[pygame.K_z]:
            

            os.system("python fight.py")
        # Сброс анимации при смене направления
        if new_direction != self.direction:
            self.direction = new_direction
            self.current_frame = 0
            self.frame_counter = 0
            self.image = self.images[self.direction][self.current_frame]

        # Обновление анимации только при движении
        if moving:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.current_frame = (self.current_frame + 1) % len(self.images[self.direction])
                self.image = self.images[self.direction][self.current_frame]
                self.frame_counter = 0
        else:
            # Остановить анимацию, вернувшись к первому кадру
            self.current_frame = 0
            self.image = self.images[self.direction][self.current_frame]
