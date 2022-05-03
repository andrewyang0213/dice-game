from tkinter import *
from tkinter import font
import mysql.connector
import tkinter as tk
import random
from PIL import ImageTk, Image

import DBHelper.LeaderboardTable.gen_lead_tb as LBGen
import DBHelper.LeaderboardTable.ins_lead_tb as LBins
import init_dice as initD

#/Users/andrewyang/Desktop/Spring Semester/Randomness/dice-game/GUI/imgs/

imagePath = "imgs/"

# Initialize Leaderboard Db
LBGen.gen_lead_tb()


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.parent = tk.Frame(self)
        # Configure root window
        self.title('Bar Dice Game')
        # Open window fullscreen
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry("%dx%d" % (self.width, self.height))
        # Show Background using label
        self.image = ImageTk.PhotoImage(Image.open(
            imagePath + "background.png").resize((self.width, self.height)))
        self.background = Label(self, image=self.image)
        self.background.place(x=0, y=0)
        # Fetch all classes
        self.header = Header(self, self.parent, *args, **kwargs)
        self.rules = Rules(self, self.parent, *args, **kwargs)
        self.user = User(self, self.parent, *args, **kwargs)
        self.dice = Dice(self, self.parent, *args, **kwargs)
        self.computer = Computer(self, self.parent, *args, **kwargs)
        self.leaderboard = Leaderboard(self, self.parent, *args, **kwargs)


class Header(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # Create Header
        font = tk.font.Font(family="Comic Sans MS", size=40, weight='bold')
        self.label = Label(parent, text=" Bar Dice Game ", font=font,
                           borderwidth=7, relief='solid')
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)


class Rules(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # Create Rules Frame
        rulesFWidth, rulesFHeight = 420, 600
        self.frame = Frame(parent, width=rulesFWidth,
                           height=rulesFHeight, bd=7, relief='solid')
        self.frame.place(relx=0.175, rely=0.5, anchor=CENTER)
        # Create Rules Header
        headerFont = tk.font.Font(
            family="Comic Sans MS", size=40, weight='bold')
        self.label = tk.Label(self.frame, text=" Rules ",
                              font=headerFont, borderwidth=4, relief='solid')
        self.label.place(relx=0.5, rely=0.15, anchor=CENTER)
        # Create Rules Text
        rule1 = "Roll the dice and guess how many pips there are in total."
        rule2 = "Make a move! For example, you can say, 5x4s, or you can choose to open if you don't believe your opponent."
        rule3 = "Make a move again after your opponent makes their move."
        rule4 = "Good luck!"

        ruleFont = tk.font.Font(family="Comic Sans MS", size=17, weight="bold")
        bullet_width = ruleFont.measure("-  ")
        em = ruleFont.measure("m")
        text = Text(self.frame, font=ruleFont, height=15, width=35,
                    relief='flat', bg=self.frame.cget('bg'), wrap=WORD)
        text.tag_configure("bulleted", lmargin1=em, lmargin2=em + bullet_width)

        text.insert("end", "1. " + rule1 + '\n' + '\n', "bulleted")
        text.insert("end", "2. " + rule2 + '\n' + '\n', "bulleted")
        text.insert("end", "3. " + rule3 + '\n' + '\n', "bulleted")
        text.insert("end", "4. " + rule4, "bulleted")
        text.place(relx=0.5, rely=0.6, anchor=CENTER)


class User(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # Create User Frame
        uFWidth, uFHeight = 375, 100
        self.frame = Frame(parent, width=uFWidth,
                           height=uFHeight, bd=4, relief='solid')
        self.frame.place(relx=0.5, rely=0.225, anchor=CENTER)
        # Create User Name
        font = tk.font.Font(family="Comic Sans MS", size=15, weight='bold')
        self.label = Label(self.frame, text=" Input User: ",
                           font=font, borderwidth=2, relief='solid')
        self.label.place(relx=0.20, rely=0.275, anchor=CENTER)
        self.entry = Entry(self.frame, width=13, font=font)
        self.entry.place(relx=0.375, rely=0.275, anchor=W)
        # Create popUp check
        popUpFont = tk.font.Font(
            family="Comic Sans MS", size=11, weight='bold')
        self.popUp = tk.StringVar()
        self.checkLabel = Label(
            self.frame, textvariable=self.popUp, font=popUpFont, width=11)
        self.checkLabel.place(relx=0.88, rely=0.275, anchor=CENTER)
        self.popUp.set(" ")
        # Create add User Data Button
        self.button = tk.Button(self.frame,  text='Add User', font=font,
                                width=10, command=lambda: self.addData())
        self.button.config(highlightthickness=0)
        self.button.place(relx=0.5, rely=0.7, anchor=CENTER)
    # Create data validation & mysql connection

    def addData(self):
        flag_validation = True  # set the flag
        self.my_name = self.entry.get()  # read name
        # length of my_name < 2 or my_name contains numbers
        if(len(self.my_name) < 2) or any(str.isdigit(c) for c in self.my_name):
            flag_validation = False
        if(flag_validation):
            LBins.ins_lead_tb([self.my_name])
        else:
            self.popUp.set("Invalid Input")
            self.checkLabel.config(fg='red')   # foreground color
            self.checkLabel.config(bg='yellow')  # background color
            self.checkLabel.config(borderwidth=2, relief='solid')


class Dice(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # Create Dice Frame
        dFWidth, dFHeight = 375, 400
        self.frame = Frame(parent, width=dFWidth,
                           height=dFHeight, bd=4, relief='solid')
        self.frame.place(relx=0.5, rely=0.525, anchor=CENTER)
        # Create Dice List
        self.diceList = initD.init_dice()
        # Create Roll Button
        font = tk.font.Font(
            family="Comic Sans MS", size=15, weight='bold')
        self.button = Button(self.frame, text='Roll Dice!', font=font,
                             bd='10', command=self.roll)
        self.button.place(relx=0.5, rely=0.55, anchor=CENTER)
        # Create User Game input
        inputFont = tk.font.Font(
            family="Comic Sans MS", size=15, weight='bold')
        self.label = Label(self.frame, text=" What's Your Move?: ",
                           font=inputFont, borderwidth=3, relief='solid')
        self.label.place(relx=0.5, rely=0.68, anchor=CENTER)
        self.entry = Entry(self.frame)
        self.entry.place(relx=0.5, rely=0.775, anchor=CENTER)
        # Create confirm input button
        self.confirm = Button(self.frame, text='Confirm Move', font=inputFont,
                              bd='10', command=self.getUserInput)
        self.confirm.place(relx=0.5, rely=0.88, anchor=CENTER)
    # Create Roll Function

    def roll(self):
        labelList = []
        xVal, yVal = 0.4, 0.125
        if len(labelList) != 0:
            for i in range(len(labelList)):
                labelList[i].destroy()
        for i in range(5):
            randomDice = self.diceList[random.randint(1, 6) - 1]
            self.label = Label(self.frame, image=randomDice)
            labelList.append(self.label)
            self.label.place(relx=xVal, rely=yVal, anchor=CENTER)
            if i % 2 == 0:
                xVal += 0.2
            else:
                if i != 3:
                    xVal -= 0.2
                else:
                    xVal -= 0.1
                yVal += 0.15
    # Get user input

    def getUserInput(self):
        self.entry.get()


class Computer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # Create AI Frame
        aiFWidth, aiFHeight = 375, 100
        self.frame = Frame(parent, width=aiFWidth,
                           height=aiFHeight, bd=4, relief='solid')
        self.frame.place(relx=0.5, rely=0.825, anchor=CENTER)
        # Create AI Move Header
        aiHeaderFont = tk.font.Font(
            family="Comic Sans MS", size=15, weight='bold')
        self.headerLabel = Label(self.frame, text=" Computer's Move: ",
                                 font=aiHeaderFont, borderwidth=3, relief='solid')
        self.headerLabel.place(relx=0.5, rely=0.275, anchor=CENTER)
        # Create AI Move Entry
        self.move = tk.StringVar()
        self.moveLabel = Label(
            self.frame, textvariable=self.move, font=aiHeaderFont)
        self.moveLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.move.set(" ")
    # Get AI Move

    def getAIMove(self):
        self.moveLabel.config(borderwidth=3, relief='solid')
        self.move.set(" Invalid Input ")


class Leaderboard(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        # Create Leaderboard Frame
        lbFWidth, lbFHeight = 400, 600
        self.frame = Frame(parent, width=lbFWidth,
                           height=lbFHeight, bd=7, relief='solid')
        self.frame.place(relx=0.825, rely=0.5, anchor=CENTER)
        # Create Leaderboard Header
        headerFont = tk.font.Font(
            family="Comic Sans MS", size=40, weight='bold')
        self.label = Label(self.frame, text=" LeaderBoard ", font=headerFont,
                           borderwidth=4, relief='solid')
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)
        # Create Refresh Leaderboard button
        font = tk.font.Font(
            family="Comic Sans MS", size=15, weight='bold')
        btn = Button(self.frame, text='Refresh', font=font, bd=1,
                     command=self.select_lead_tb)
        btn.place(relx=0.75, rely=0.19, anchor=CENTER)
    # Create Leaderboard Widget

    def select_lead_tb(self):
        conn = mysql.connector.connect(
            user='root', password='ubercharge1', host='localhost', database='dice_game')
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT * FROM LEADERBOARD where PLAYER > '' limit 0,10''')

        xVal, yVal = 0.15, 0.25
        self.columnNames = ["Rank", "Player", "Wins", "Win %", "Games"]
        for columnName in self.columnNames:
            self.nameRow = Label(self.frame, width=7, text=columnName,
                                 relief='solid', anchor='c')
            self.nameRow.place(relx=xVal, rely=yVal, anchor=CENTER)
            xVal += 0.25

        xVal = 0.15
        yVal += 0.05
        for fields in cursor:
            for j in range(1, len(fields)):
                self.eRow = Label(self.frame, width=7,
                                  text=fields[j], relief='flat', anchor='c')
                self.eRow.place(relx=xVal, rely=yVal, anchor=CENTER)
                xVal += 0.25
            xVal = 0.15
            yVal += 0.05
        conn.close()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
