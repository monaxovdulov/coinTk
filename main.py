from tkinter import *
import random


def create_coin():
  x = random.randint(20, 100)
  y = random.randint(20, 100)
  canvas.create_oval(x, y, x + 20, y + 20, fill="gold")

# Функция для подсчета очков при клике на монету
def collect_coin(event):
    items = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    if items:
        canvas.delete(items[0])
        update_score(1)

# Функция для обновления счета
def update_score(points):
    global score
    score += points
    score_label.config(text=f"Счет: {score}")

root = Tk()
root.geometry("400x300")

# Создаем холст для отображения монет
canvas = Canvas(root, width=150, height=100, bg="lightblue")
canvas.pack()

btn1 = Button(text="Создать монету", command=create_coin,)
btn1.pack()

# Создаем метку для отображения счета
score = 0
score_label = Label(root, text="Счет: 0")
score_label.pack()

# Привязываем клик мыши к функции сбора монет
canvas.bind("<Button-1>", collect_coin)

root.mainloop()
