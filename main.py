from tkinter import *
# create a tkinter window
from PIL import ImageTk, Image
import mysql.connector

import tkinter as tk
import random

import DBHelper.LeaderboardTable.gen_lead_tb as LBGen
import DBHelper.LeaderboardTable.ins_lead_tb as LBins


# Initialize Leaderboard Db
LBGen.gen_lead_tb()


window = tk.Tk()

# set window name
window.title('Bar Dice Game')

# Open window having dimension 100x100
window.geometry('1000x1000')

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
        label = Label(image=randomDice)
        labelList.append(label)
        label.place(x=xVal, y=yVal)
        if i % 2 == 0:
            xVal += 65
        else:
            if i != 3:
                xVal -= 65
            else:
                xVal -= 32.5
            yVal += 60


# Create Header
headerFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
header = Label(window, text="Bar Dice Game", font=headerFont,
               borderwidth=3, relief='solid')
header.pack()

# Create Leaderboard Header
LBHeaderFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
LBHeader = Label(window, text="LeaderBoard", font=headerFont,
                 borderwidth=3, relief='solid')
LBHeader.place(x=700, y=100)

# Create User Name
userNameFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userName = Label(window, text="Input User",
                 font=userNameFont).place(x=30, y=80)
userNameEntry = Entry(window)
userNameEntry.place(x=130, y=80)
my_str = tk.StringVar()
l5 = tk.Label(window, textvariable=my_str, width=10)
l5.pack()
my_str.set("Output")

# Create add User Data Button
b1 = tk.Button(window,  text='Add Record',
               width=10, command=lambda: add_data())
b1.pack()

# Create data validation & mysql connection


def add_data():
    flag_validation = True  # set the flag
    my_name = userNameEntry.get()  # read name
    # my_class=options.get()    # read class
    # my_mark=t3.get("1.0",END) # read mark
    # my_gender=radio_v.get()   # read gender

    # length of my_name , my_class and my_gender more than 2
    if(len(my_name) < 2):  # or len(my_class)<2  or len(my_gender) < 2 ):
        flag_validation = False

    if(flag_validation):
        LBins.ins_lead_tb([my_name])
    else:
        l5.config(fg='red')   # foreground color
        l5.config(bg='yellow')  # background color
        my_str.set("check inputs.")

# Create Leaderboard Widget


def select_lead_tb():
    conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game')
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT PLAYER FROM LEADERBOARD where PLAYER > '' limit 0,10''')
    i = 0
    for fields in cursor:
        for j in range(len(fields)):
            e = Entry(window, width=10, fg='blue')
            e.place(x=700, y=150)  # grid(row=i, column=j)
            e.insert(END, fields[j])
        i = i+1
    conn.close()


select_lead_tb()

# Create Refresh Leaderboard button
btn = Button(window, text='Refresh', bd='10', command=select_lead_tb)
btn.place(x=900, y=180)

# Create Roll Button
btn = Button(window, text='Roll!', bd='10', command=roll)
btn.place(x=130, y=120)

# Create User Game input
userGInputFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userGInput = Label(window, text="What's your move?: ",
                   font=userNameFont).place(x=30, y=350)
userGInputEntry = Entry(window).place(x=30, y=380)

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
