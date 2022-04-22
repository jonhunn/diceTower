import random as r
import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar
from tkinter import OptionMenu


# number of dice to roll
options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

###### functions for random rolls ######


def coinFlip():
    total = r.randint(1, 2)
    if total % 2 == 0:
        messagebox.showinfo("Message", "Coin Flip: \n Heads")
    else:
        messagebox.showinfo("Message", "Coin Flip: \n Tails")


def rollD4():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 4)
        total += bone
        bones.append(bone)

    total = ("D4:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


def rollD6():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 6)
        total += bone
        bones.append(bone)

    total = ("D6:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


def rollD8():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 8)
        total += bone
        bones.append(bone)

    total = ("D8:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


def rollD10():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 10)
        total += bone
        bones.append(bone)

    total = ("D10:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


def rollD12():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 12)
        total += bone
        bones.append(bone)

    total = ("D12:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


def rollD20():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 20)
        total += bone
        bones.append(bone)

    total = ("D20:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


def rollD100():
    total = 0
    bones = []

    for i in range(howMany.get()):
        bone = r.randint(1, 100)
        total += bone
        bones.append(bone)

    total = ("D100:\n" + str(bones) + "\n total:" + str(total))
    messagebox.showinfo("Message", total)


# creates window
window = tk.Tk()
window.title("Dungeon Dice Roll!")
window.geometry("210x250")

# setting up the dropdown menu ("How many dice?")
howMany = IntVar()
howMany.set(options[0])

dropDown = OptionMenu(window, howMany, *options)
dropDown.pack()

# buttons on the window
coinButton = tk.Button(window, text="Coin Flip", command=coinFlip)
coinButton.pack()

d4Button = tk.Button(window, text="D4", command=rollD4)
d4Button.pack()

d6Button = tk.Button(window, text="D6", command=rollD6)
d6Button.pack()

d8Button = tk.Button(window, text="D8", command=rollD8)
d8Button.pack()


d10Button = tk.Button(window, text="D10", command=rollD10)
d10Button.pack()


d12Button = tk.Button(window, text="D12", command=rollD12)
d12Button.pack()


d20Button = tk.Button(window, text="D20", command=rollD20)
d20Button.pack()

d100Button = tk.Button(window, text="D100", command=rollD100)
d100Button.pack()

window.mainloop()
