import tkinter as tk
from tkinter import font, messagebox
import pygame
import re
import os
from funcs import open_terminal
# Создаем главное окно
root = tk.Tk()
root.geometry("1200x900")
root.resizable(False,False)
root.configure(bg="black")
root.title("Undertale ~ Set Name")

icon = tk.PhotoImage(file='Assets/img/icons/b_heart.png') 
root.iconphoto(True, icon)

pygame.mixer.init()
try:
    pygame.mixer.music.load("Assets/sounds/soundtracks/waterfall.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
except pygame.error:
    print("Music file not found!")

pixel_font = font.Font(family="Courier", size=20)

question_label = tk.Label(root, text="What's your name?", font=pixel_font, bg="black", fg="white")
question_label.place(x=420, y=250)

name_entry = tk.Entry(root, font=pixel_font, width=30, bg="black", fg="yellow", justify="center", bd=0, highlightthickness=0, insertbackground="yellow")
name_entry.place(x=300, y=350)


def submit_name():
    name_user = name_entry.get()
    
    if len(name_user) > 6 or not re.match("^[A-Za-zА-Яа-я]+$", name_user):
        messagebox.showerror("Error", "The name must not contain random characters and must be shorter than 7 characters.")
    else:
        with open("user_name.txt", "w") as file:
            file.write(name_user)
        pygame.mixer.stop()
        root.destroy()
        open_terminal("python game.py")
        
done_label = tk.Label(root, text="Done", font=pixel_font, bg="black", fg="white", cursor="hand2")
done_label.place(x=550, y=450)

def on_enter(event):
    done_label.config(fg="yellow")

def on_leave(event):
    done_label.config(fg="white")

# Привязываем события к метке
done_label.bind("<Enter>", on_enter)
done_label.bind("<Leave>", on_leave)
done_label.bind("<Button-1>", lambda event: submit_name())  

root.mainloop()
