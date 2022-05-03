from tkinter import *
# create a tkinter window
from tkinter import font
import mysql.connector
import tkinter as tk
import random
from PIL import ImageTk, Image

''' import DBHelper.LeaderboardTable.gen_lead_tb as LBGen
import DBHelper.LeaderboardTable.ins_lead_tb as LBins '''

import init_dice as initD


# Initialize Leaderboard Db
''' LBGen.gen_lead_tb() '''

# Initialize Tkinter obj
window = tk.Tk()

# set window name
window.title('Bar Dice Game')

# Open window fullscreen
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

''' # Open window having dimension 100x100
window.geometry('1000x1000') '''

#/Users/andrewyang/Desktop/Spring Semester/Randomness/dice-game/GUI/

imagePath = "imgs/"

bg = ImageTk.PhotoImage(Image.open(imagePath + "background.png").resize((width, height)))

# Show Background using label
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

''' def show_computer(label,button):
   label.pack()
   button.configure(command=hide_computer())
def hide_computer(label, button):
   label.pack_forget()
   button.configure(command=show_computer()) '''

# Create Header
headerFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
header = Label(window, text=" Bar Dice Game ", font=headerFont,
               borderwidth=4, relief='solid')
header.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create Rules Frame
rulesFWidth, rulesFHeight = 420, 600
rulesFrame = Frame(window, width = rulesFWidth, height = rulesFHeight, bd = 4, relief = 'solid')
rulesFrame.place(relx = 0.175, rely = 0.5, anchor=CENTER)

# Create Rules Header
rulesHeaderFont = tk.font.Font(family= "Comic Sans MS", size=40, weight='bold')
rulesHeader = Label(rulesFrame, text= " Rules ", font = rulesHeaderFont, borderwidth=4, relief='solid')
rulesHeader.place(relx=0.5, rely=0.15, anchor=CENTER)

# Create Rules Text
rule1 = "Roll the dice and guess how many pips there are in total."
rule2 = "Make a move! For example, you can say, 5x4s, or you can choose to open if you don't believe your opponent."
rule3 = "Make a move again after your opponent makes their move."
rule4 = "Good luck!"

ruleFont = tk.font.Font(family ="Comic Sans MS", size = 17, weight = "bold")
bullet_width = ruleFont.measure("-  ")
em = ruleFont.measure("m")
text = Text(rulesFrame, font = ruleFont, height=15, width=35, relief='flat', bg = rulesFrame.cget('bg'), wrap = WORD)
text.tag_configure("bulleted", lmargin1 = em, lmargin2 = em + bullet_width)

text.insert("end", "1. " + rule1 + '\n' + '\n', "bulleted")
text.insert("end", "2. " + rule2 + '\n' + '\n', "bulleted")
text.insert("end", "3. " + rule3 + '\n' + '\n', "bulleted")
text.insert("end", "4. " + rule4, "bulleted")
text.place(relx=0.5, rely=0.6, anchor=CENTER)

# Create User Frame
uFWidth, uFHeight = 375, 100
userFrame = Frame(window, width = uFWidth, height = uFHeight, bd = 4, relief = 'solid')
userFrame.place(relx = 0.5, rely = 0.225, anchor=CENTER)

# Create User Name
userNameFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userName = Label(userFrame, text=" Input User: ",
                 font=userNameFont, borderwidth=2, relief='solid').place(relx=0.20, rely=0.275, anchor=CENTER)
userNameEntry = Entry(userFrame, width = 15, font = userNameFont)
userNameEntry.place(relx=0.375, rely=0.275, anchor=W)

''' my_str = tk.StringVar()
#error = Label(window, textvariable=my_str, width= 7)
canvasWidth, canvasHeight = 60, 30
errorCanvas = Canvas(userFrame, width = canvasWidth, height = canvasHeight, highlightthickness= 0)
errorCanvas.place(relx=0.6, rely=0.2, anchor=CENTER)
error = errorCanvas.create_text((canvasWidth/2, canvasHeight/2),text = "hi", font = "ComicSansMS 15 bold", fill = "black")
r = errorCanvas.create_rectangle(errorCanvas.bbox(error), fill = "")
errorCanvas.tag_lower(r, error) '''
#my_str.set(" ")

# Create add User Data Button
''' b1 = tk.Button(window,  text='Add User',
               width=20, command=lambda: LBins.ins_lead_tb([userNameEntry.get()]))
b1.config(highlightthickness = 0)
b1.place(relx=0.5, rely=0.275, anchor=CENTER) '''

# Create data validation & mysql connection
''' def add_data():
    flag_validation = True  # set the flag
    my_name = userNameEntry.get()  # read name

    # length of my_name < 2 or my_name contains numbers
    if(len(my_name) < 2) or any(str.isdigit(c) for c in my_name):
        flag_validation = False

    if(flag_validation):
        LBins.ins_lead_tb([my_name])
    else:
        errorCanvas.itemconfigure(error, text = "Invalid Input")
        errorCanvas.itemconfigure(error, fill ='red')   # foreground color
        errorCanvas.itemconfigure(r, fill ='yellow')  # background color
        #my_str.set("Invalid Input") '''

# Create Dice Frame
dFWidth, dFHeight = 375, 400
diceFrame = Frame(window, width = dFWidth, height = dFHeight, bd = 4, relief = 'solid')
diceFrame.place(relx = 0.5, rely = 0.525, anchor=CENTER)

# Create Roll Function
labelList = []
diceList = initD.init_dice()
def roll():
    xVal, yVal = 0.4, 0.125
    if len(labelList) != 0:
        for i in range(len(labelList)):
            labelList[i].destroy()
    for i in range(5):
        randomDice = diceList[random.randint(1, 6) - 1]
        label = Label(diceFrame, image=randomDice)
        labelList.append(label)
        label.place(relx=xVal, rely=yVal, anchor=CENTER)
        if i % 2 == 0:
            xVal += 0.2
        else:
            if i != 3:
                xVal -= 0.2
            else:
                xVal -= 0.1
            yVal += 0.15

# Create Roll Button
btn = Button(diceFrame, text='Roll Dice!', bd='10', command=roll)
btn.place(relx=0.5, rely=0.55, anchor=CENTER)

# Create User Game input
userGInputFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
userGInput = Label(diceFrame, text=" What's Your Move?: ",
                   font=userGInputFont, borderwidth=3, relief='solid').place(relx=0.5, rely=0.675, anchor=CENTER)
userGInputEntry = Entry(diceFrame)
userGInputEntry.place(relx=0.5, rely=0.775, anchor=CENTER)

def getUserInput():
    print(userGInputEntry.get())
    return userGInputEntry.get()

# Create Confirm Input Button
def confirmInput():
    btn = Button(diceFrame, text='Confirm Move', bd='10', command=getUserInput)
    btn.place(relx=0.5, rely=0.875, anchor=CENTER)

confirmInput()

# Create AI Frame
aiFWidth, aiFHeight = 375, 100
aiFrame = Frame(window, width = aiFWidth, height = aiFHeight, bd = 4, relief = 'solid')
aiFrame.place(relx = 0.5, rely = 0.825, anchor=CENTER)

# Create AI Move Header
aiHeaderFont = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
aiHeader = Label(aiFrame, text=" Computer's Move: ", font=aiHeaderFont, borderwidth=3, relief='solid')
aiHeader.place(relx=0.5, rely=0.275, anchor=CENTER)

# Create AI Move Entry
aiMove = tk.StringVar()
aiMoveLabel = Label(aiFrame, textvariable= aiMove, font = aiHeaderFont)
aiMoveLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
aiMove.set(" ")

# Get AI Move
def getAIMove():
    aiMoveLabel.config(borderwidth = 3, relief = 'solid')
    aiMove.set(" Invalid Input ")

# Create Leaderboard Frame
lbFWidth, lbFHeight = 400, 600
lBoardFrame = Frame(window, width = lbFWidth, height = lbFHeight, bd = 4, relief = 'solid')
lBoardFrame.place(relx = 0.825, rely = 0.5, anchor=CENTER)

# Create Leaderboard Header
LBHeaderFont = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
LBHeader = Label(lBoardFrame, text=" LeaderBoard ", font=headerFont,
                 borderwidth=4, relief='solid')
LBHeader.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create Leaderboard Widget
def select_lead_tb():
    conn = mysql.connector.connect(
        user='root', password='ubercharge1', host='localhost', database='dice_game')
    cursor = conn.cursor()
    cursor.execute(
        '''SELECT * FROM LEADERBOARD where PLAYER > '' limit 0,10''')

    xVal, yVal = 0.15, 0.25
    columnNames = ["Rank", "Player", "Wins", "Win %", "Games"]
    for columnName in columnNames:
        nameRow = Label(lBoardFrame, width=7, text=columnName,
                        relief='flat', anchor='c')
        nameRow.place(relx=xVal, rely=yVal, anchor=CENTER)
        xVal += 0.25

    xVal = 0.15
    yVal += 0.05
    for fields in cursor:
        for j in range(1, len(fields)):
            eRow = Label(lBoardFrame, width=7,
                         text=fields[j], relief='flat', anchor='c')
            eRow.place(relx=xVal, rely=yVal, anchor=CENTER)
            xVal += 0.25
        xVal = 0.15
        yVal += 0.05
    conn.close()

''' select_lead_tb() '''

''' # Create Refresh Leaderboard button
btn = Button(lBoardFrame, text='Refresh', bd= 1, command=select_lead_tb)
btn.place(relx=0.75, rely=0.185, anchor=CENTER)
 '''

#window.update()
window.mainloop()
