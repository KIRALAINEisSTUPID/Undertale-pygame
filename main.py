import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import pygame

# Инициализация pygame для воспроизведения музыки
pygame.mixer.init()
try:
    pygame.mixer.music.load("Assets/sounds/soundtracks/1.02 Le Souvenir avec le crepuscule.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
except pygame.error:
    print("Music file not found!")

# Создание главного окна
window = tk.Tk()
window.title("Undertale * Menu")
window.geometry("1200x900")
window.resizable(False,False)
icon = tk.PhotoImage(file='Assets/img/icons/b_heart.png')  # You can use .png or .gif
window.iconphoto(True, icon)
# Загрузка фона
background_image = Image.open("Assets/img/backgrounds/menu_bg.png")
background_image = background_image.resize((1200, 900))
background_photo = ImageTk.PhotoImage(background_image)

# Добавление фона
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Использование шрифта Courier (стандартный моноширинный шрифт)
pixel_font = font.Font(family="Courier", size=20)  # Моноширинный шрифт

# Функция для изменения цвета текста в зависимости от положения курсора
def on_enter(event, label):
    label.config(fg="yellow")

def on_leave(event, label):
    label.config(fg="white")

# Функция для действия при нажатии на "кнопку"
def action1(event):
    print("Действие 1 выполнено!")

def action2(event):
    print("Действие 2 выполнено!")

# Создание меток, которые будут работать как кнопки
label1 = tk.Label(window, text="Play", bg="black", fg="white", font=pixel_font, cursor="hand2")
label1.place(x=350, y=350)
label1.bind("<Enter>", lambda e: on_enter(e, label1))  # Изменение цвета при наведении
label1.bind("<Leave>", lambda e: on_leave(e, label1))  # Восстановление цвета при выходе курсора
label1.bind("<Button-1>", action1)  # Действие при клике

label2 = tk.Label(window, text="Quit", bg="black", fg="white", font=pixel_font, cursor="hand2")
label2.place(x=700, y=350)
label2.bind("<Enter>", lambda e: on_enter(e, label2))  # Изменение цвета при наведении
label2.bind("<Leave>", lambda e: on_leave(e, label2))  # Восстановление цвета при выходе курсора
label2.bind("<Button-1>", action2)  # Действие при клике

# Запуск главного цикла приложения
window.mainloop()
