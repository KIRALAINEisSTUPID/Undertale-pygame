import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import pygame
import os
import random
import webbrowser
# Инициализация pygame для воспроизведения музыки
pygame.mixer.init()
try:
    pygame.mixer.music.load("Assets/sounds/soundtracks/1.02 Le Souvenir avec le crepuscule.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
except pygame.error:
    print("Music file not found!")

# Создание главного окна
window = tk.Tk()
window.title("Undertale ~ Menu")
window.geometry("1450x900")
window.resizable(False,False)
icon = tk.PhotoImage(file='Assets/img/icons/b_heart.png') 
window.iconphoto(True, icon)
# Загрузка фона
background_image = Image.open("Assets/img/backgrounds/menu_bg.png")
background_image = background_image.resize((1450, 900))
background_photo = ImageTk.PhotoImage(background_image)
quotes = ["Game for fun, not for money.",
          "Stay determined.",
          "Its writed on Vscode.",
          "It's a beautiful day outside... birds are singing...",
          "2+2=5",
          "has bugs which bigger than galactic",
          "did you your homewroks?",
          "when C++?",
          "windows sucks"
          "PDP academy's wifi pasword?",
          ]
# Добавление фона
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Использование шрифта Courier (стандартный моноширинный шрифт)
pixel_font = font.Font(family="Courier", size=20)  # Моноширинный шрифт

# Функция для изменения цвета текста в зависимости от положения курсора
def on_enter(event, label):
    label.config(fg="yellow", height=2)

def on_enter3(event, label):
    label.config(fg="purple")
def on_leave(event, label):
    label.config(fg="white",width=0, height=0)

# Функция для действия при нажатии на "кнопку"
def action1(event):
    pygame.mixer.music.stop()
    window.destroy()
    os.system("python player_name.py")
    
def update_quote():
    new_quote = random.choice(quotes)
    quote_label.config(text=new_quote)
    window.after(5000, update_quote)  # Обновляет цитату каждые 5 секунд
def action2(event):
    window.destroy()

def action3(event):
    webbrowser.open_new_tab("https://github.com/KIRALAINEisSTUPID/Undertale-pygame")
# Создание меток, которые будут работать как кнопки
quote_label = tk.Label(window, text=random.choice(quotes), bg="black", fg="white", font=pixel_font)
quote_label.place(x=0, y=0)
label1 = tk.Label(window, text="Play", bg="black", fg="white", font=pixel_font, cursor="hand2")
label1.place(x=300, y=350)
label1.bind("<Enter>", lambda e: on_enter(e, label1))  # Изменение цвета при наведении
label1.bind("<Leave>", lambda e: on_leave(e, label1))  # Восстановление цвета при выходе курсора
label1.bind("<Button-1>", action1)  # Действие при клике

label2 = tk.Label(window, text="Quit", bg="black", fg="white", font=pixel_font, cursor="hand2")
label2.place(x=1000, y=350)
label2.bind("<Enter>", lambda e: on_enter(e, label2))  # Изменение цвета при наведении
label2.bind("<Leave>", lambda e: on_leave(e, label2))  # Восстановление цвета при выходе курсора
label2.bind("<Button-1>", action2)  # Действие при клике


label3 =tk.Label(window, text="View code on Github♡", bg="black", fg="white", font=pixel_font, cursor="hand2")
label3.place(x=500,y=860)
label3.bind("<Enter>", lambda e: on_enter3(e, label3))  # Изменение цвета при наведении
label3.bind("<Leave>", lambda e: on_leave(e, label3))  # Восстановление цвета при выходе курсора
label3.bind("<Button-1>", action3) 
# Запуск главного цикла приложения
update_quote()
window.mainloop()
