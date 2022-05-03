from tkinter import *
from PIL import ImageTk, Image

def init_dice():
    #/Users/andrewyang/Desktop/Spring Semester/Randomness/dice-game/GUI/
    imagePath = "imgs/"

    diceList = []
    diceList.append(ImageTk.PhotoImage(
        Image.open(imagePath + "one.png").resize((50, 50))))
    diceList.append(ImageTk.PhotoImage(
        Image.open(imagePath + "two.png").resize((50, 50))))
    diceList.append(ImageTk.PhotoImage(Image.open(
        imagePath + "three.png").resize((50, 50))))
    diceList.append(ImageTk.PhotoImage(Image.open(
        imagePath + "four.png").resize((50, 50))))
    diceList.append(ImageTk.PhotoImage(Image.open(
        imagePath + "five.png").resize((50, 50))))
    diceList.append(ImageTk.PhotoImage(
        Image.open(imagePath + "six.png").resize((50, 50))))
    return diceList