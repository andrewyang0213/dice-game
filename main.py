from tkinter import *
# create a tkinter window
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font

import tkinter as tk
import random

count = 0
window = tk.Tk()

#set window name
window.title('Bar Dice Game')

# Open window having dimension 100x100
window.geometry('500x500')

imagePath = "imgs/"

diceList = []
diceList.append(ImageTk.PhotoImage(Image.open(imagePath + "one.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open(imagePath + "two.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open(imagePath + "three.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open(imagePath + "four.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open(imagePath + "five.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open(imagePath + "six.png").resize((50, 50))))
print(len(diceList))

''' def show_computer(label,button):
   label.pack()
   button.configure(command=hide_computer())
def hide_computer(label, button):
   label.pack_forget()
   button.configure(command=show_computer()) '''

labelList = []
def roll():
    xVal, yVal = 90, 170

    if len(labelList) != 0:
        for i in range(len(labelList)):
            labelList[i].destroy()

    for i in range(5):
        randomDice = diceList[random.randint(1, 6) - 1]
        label = Label(image= randomDice)
        labelList.append(label)
        label.place(x = xVal, y = yVal)
        if i % 2 == 0:
            xVal += 65
        else:
            if i != 3:
                xVal -= 65
            else:
                xVal -= 32.5
            yVal += 60


# Create Header
headerFont = tk.font.Font(family = "Comic Sans MS", size = 40, weight = 'bold')
header = Label(window, text="Bar Dice Game", font = headerFont, borderwidth= 3, relief = 'solid')
header.pack()

# Create User Name
userNameFont = tk.font.Font(family = "Comic Sans MS", size = 15, weight = 'bold')
userName = Label(window, text="Input User", font = userNameFont).place(x = 30, y = 80)
userNameEntry = Entry(window).place(x = 130, y = 80)

# Create a Button
btn = Button(window, text='Roll!', bd='10', command=roll)
btn.place(x = 130, y = 120)

# Create User Game input
userGInputFont = tk.font.Font(family = "Comic Sans MS", size = 15, weight = 'bold')
userGInput = Label(window, text="What's your move?: ", font = userNameFont).place(x = 30, y = 350)
userGInputEntry = Entry(window).place(x = 30, y = 380)


window.mainloop()

''' game_frame = Frame(window)
game_frame.pack()

my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id",anchor=CENTER, width=80)
my_game.column("player_name",anchor=CENTER,width=80)
my_game.column("player_Rank",anchor=CENTER,width=80)
my_game.column("player_states",anchor=CENTER,width=80)
my_game.column("player_city",anchor=CENTER,width=80)

my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("player_id",text="Id",anchor=CENTER)
my_game.heading("player_name",text="Name",anchor=CENTER)
my_game.heading("player_Rank",text="Rank",anchor=CENTER)
my_game.heading("player_states",text="States",anchor=CENTER)
my_game.heading("player_city",text="States",anchor=CENTER)

my_game.insert(parent='',index='end',iid=0,text='',
values=('1','Ninja','101','Oklahoma', 'Moore'))
my_game.insert(parent='',index='end',iid=1,text='',
values=('2','Ranger','102','Wisconsin', 'Green Bay'))
my_game.insert(parent='',index='end',iid=2,text='',
values=('3','Deamon','103', 'California', 'Placentia'))
my_game.insert(parent='',index='end',iid=3,text='',
values=('4','Dragon','104','New York' , 'White Plains'))
my_game.insert(parent='',index='end',iid=4,text='',
values=('5','CrissCross','105','California', 'San Diego'))
my_game.insert(parent='',index='end',iid=5,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))

my_game.insert(parent='',index='end',iid=6,text='',
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY')) '''



''' my_game.pack() '''
