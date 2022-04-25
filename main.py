from tkinter import *
# create a tkinter window
from PIL import ImageTk, Image
from tkinter import ttk
import random

count = 0
root = Tk()

# Open window having dimension 100x100
root.geometry('100x100')

diceList = []
diceList.append(ImageTk.PhotoImage(Image.open("one.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open("two.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open("three.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open("four.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open("five.png").resize((50, 50))))
diceList.append(ImageTk.PhotoImage(Image.open("six.png").resize((50, 50))))
print(len(diceList))

def show_computer(label,button):
   label.pack()
   button.configure(command=hide_computer())
def hide_computer(label, button):
   label.pack_forget()
   button.configure(command=show_computer())

labelList = []
def roll():
    if len(labelList) != 0:
        for i in range(len(labelList)):
            labelList[i].destroy()

    for i in range(5):
        label = Label(image=diceList[random.randint(1, 6) - 1])
        labelList.append(label)
        label.pack()
    labelList.append(Text(root, height=1, width=10, bg="light yellow"))
    labelList[len(labelList)-1].pack()




# Create a Button
btn = Button(root, text='Roll!', bd='5',
             command=roll)

game_frame = Frame(root)
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
values=('6','ZaqueriBlack','106','Wisconsin' , 'TONY'))



header = Label(root, text="SHAI ZI", bg="yellow")
header.pack()
btn.pack()
my_game.pack()

root.mainloop()