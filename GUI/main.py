from tkinter import *
# create a tkinter window
from tkinter import font
import mysql.connector
import tkinter as tk
import random
from PIL import ImageTk, Image

import DBHelper.LeaderboardTable.gen_lead_tb as LBGen
import DBHelper.LeaderboardTable.ins_lead_tb as LBins
import init_dice as initD


# Initialize Leaderboard Db
""" LBGen.gen_lead_tb() """

# Initialize Tkinter obj
window = tk.Tk()

# set window name
window.title('Bar Dice Game')

# Open window fullscreen
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))

''' # Open window having dimension 100x100
window.geometry('1000x1000') '''



bg = ImageTk.PhotoImage(Image.open("imgs/background.png").resize((width, height)))
  
# Show image using label
label1 = Label(window, image = bg)
label1.place(x = 0, y = 0)

''' def show_computer(label,button):
   label.pack()
   button.configure(command=hide_computer())
def hide_computer(label, button):
   label.pack_forget()
   button.configure(command=show_computer()) '''


diceList = initD.init_dice()

# Create Roll Function
labelList = []

def roll():
    xVal, yVal = 0.45, 0.35

    if len(labelList) != 0:
        for i in range(len(labelList)):
            labelList[i].destroy()

    for i in range(5):
        print(i)
        print(xVal, yVal)
        randomDice = diceList[random.randint(1, 6) - 1]
        label = Label(image=randomDice)
        labelList.append(label)
        label.place(relx=xVal, rely=yVal, anchor = CENTER)
        if i % 2 == 0:
            xVal += 0.1
        else:
            if i != 3:
                xVal -= 0.1
            else:
                xVal -= 0.05
            yVal += 0.1

# Create Header
headerFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
header = Label(window, text=" Bar Dice Game ", font=headerFont,
               borderwidth=4, relief='solid')
header.place(relx = 0.5, rely = 0.1, anchor = CENTER)

# Create Rules Header and Rules text widget
headerFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
header = Label(window, text=" Rules ", font=headerFont,
               borderwidth=4, relief='solid')
header.place(relx = 0.15, rely = 0.1, anchor = CENTER)


# Create text widget and specify size.
T = Text(window, height = 8, width = 35)
 
Rules = """1.Roll and guess how many dices are there in total.
2.Make a move! for example, you can say, 5x4s, or open the cups. 
3.Make a move again after the computer makes its move.
4.Good luck!"""
Font_tuple = ("Comic Sans MS", 17, "bold")
T.configure(font = Font_tuple)
T.insert(tk.END, Rules)
T.place(relx = 0.15, rely = 0.3, anchor = CENTER)

# Create Leaderboard Header
LBHeaderFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
LBHeader = Label(window, text=" LeaderBoard ", font=headerFont,
                 borderwidth=4, relief='solid')
LBHeader.place(relx=0.8, rely=0.1, anchor=CENTER)

# Create User Name
userNameFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userName = Label(window, text="Input User",
                 font=userNameFont, borderwidth=4, relief='solid').place(relx=0.4, rely=0.2, anchor = CENTER)
userNameEntry = Entry(window)
userNameEntry.place(relx = 0.5, rely= 0.2, anchor=CENTER)
my_str = tk.StringVar()
l5 = tk.Label(window, textvariable=my_str, width=10)
l5.place(relx = 0.6, rely= 0.2, anchor=CENTER)
my_str.set(" ")

# Create add User Data Button
""" b1 = tk.Button(window,  text='Add User',
               width=10, command=lambda: add_data())
b1.place(relx = 0.5, rely = 0.25, anchor=CENTER) """

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
        my_str.set("Invalid Input")

# Create Leaderboard Widget
def select_lead_tb():
    conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game')
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT PLAYER FROM LEADERBOARD where PLAYER > '' limit 0,10''')
    i = 0
    xVal, yVal= 0.8, 0.25
    for fields in cursor:
        for j in range(len(fields)):
            e = Entry(window, width=10, fg='blue')
            e.place(relx = xVal, rely= yVal, anchor=CENTER)
            e.insert(END, fields[j])

        i = i+1
    conn.close()

""" select_lead_tb() """

# Create Refresh Leaderboard button
btn = Button(window, text='Refresh', bd='10', command=select_lead_tb)
btn.place(relx = 0.875, rely= 0.17, anchor= CENTER)

# Create Roll Button
btn = Button(window, text='Roll Dice!', bd='10', command=roll)
btn.place(relx = 0.5, rely= 0.7, anchor=CENTER)

# Create User Game input
userGInputFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userGInput = Label(window, text="What's Your Move?: ",
                   font=userNameFont, borderwidth=3, relief='solid').place(relx = 0.5, rely= 0.75, anchor=CENTER)
userGInputEntry = Entry(window).place(relx = 0.5, rely= 0.8, anchor=CENTER)

# Create User Input Button
btn = Button(window, text='Confirm Move', bd='10', command=roll)
btn.place(relx = 0.5, rely= 0.85, anchor=CENTER)

# Create AI Move Header
userGInputFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userGInput = Label(window, text="Computer's Move: ",
                   font=userNameFont, borderwidth=3, relief='solid').place(relx = 0.5, rely= 0.9, anchor=CENTER)


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
