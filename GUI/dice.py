from tkinter import *
from PIL import ImageTk, Image


def init_dice():
    # /Users/andrewyang/Desktop/Spring Semester/Randomness/dice-game/GUI/
    imagePath = "GUI/imgs/"

    diceList = []

    dice1 = Image.open(imagePath + "one.png").resize((50, 50))
    dice2 = Image.open(imagePath + "two.png").resize((50, 50))
    dice3 = Image.open(imagePath + "three.png").resize((50, 50))
    dice4 = Image.open(imagePath + "four.png").resize((50, 50))
    dice5 = Image.open(imagePath + "five.png").resize((50, 50))
    dice6 = Image.open(imagePath + "six.png").resize((50, 50))

    diceList.append(ImageTk.PhotoImage(dice1))
    diceList.append(ImageTk.PhotoImage(dice2))
    diceList.append(ImageTk.PhotoImage(dice3))
    diceList.append(ImageTk.PhotoImage(dice4))
    diceList.append(ImageTk.PhotoImage(dice5))
    diceList.append(ImageTk.PhotoImage(dice6))
    return diceList
