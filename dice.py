import random

import gen_table
import populate_table

from scipy.special import binom, factorial

d1 = []
d2 = []
current = [0,0]

while(len(set(d1)) == len(d1)):
    d1 = []
    for i in range(0, 5):
        n = random.randint(1, 6)
        d1.append(n)
        
while(len(set(d2)) == len(d2)):
    d2 = []
    for i in range(0, 5):
        n = random.randint(1, 6)
        d2.append(n)

def open(d1, d2, n, k):
    count = 0
    for x in range(0, 5):
        if(d1[x] == k or d1[x] == 1):
            count += 1
        if(d2[x] == k or d2[x] == 1):
            count += 1
    if(len(set(d1)) == 1 and k == d1[0]):
        count += 1
    elif(len(set(d1)) == 2 and set(d1) == {1, k}):
        count += 1
    if(len(set(d2)) == 1 and k == d2[0]):
        count += 1
    elif(len(set(d2)) == 2 and set(d2) == {1, k}):
        count += 1
    if(count >= n):
        return True
    return False
    
def check(current, n, k):
    if(n not in range(3, 14) or k not in range(1, 7)):
        print("Out of range or wrong type of data.")
        return False
    elif(current[0] > n):
        print("The number must be larger than the one in the previous round.")
        return False
    elif((current[0] == n and current[1] >= k and k >= 2) or (current[0] == n and current[1] == 1)):
        print("The value must be larger than the one in the previous round if the number keeps the same.")
        return False
    else:
        current = [n,k]
        return True

if __name__ == '__main__':
    gen = gen_table.generate_table()
    print("Welcome to the BAR DICE!")
    rounds = int(input("How any rounds would you like to play?"))
    counter = 0
    while rounds not in range(3, 11):
        rounds = int(input("INVALID INPUT. Out of range or wrong type of data. Try again: "))
    if rounds in range(3, 11):
        print ("Challenge accepted! I will play you for", rounds,"rounds! Let's begin!!!")
        
        
    while counter <= rounds - 1:
        opened = False
        count = 0
        print("YOUR DICE: ",d1)
        
        while(not opened):
            win = 0
            winner = ""
            if(count > 0) and input("Do you want to open? y/n") == "y":
                if open(d1, d2, current[0], current[1]):
                    print("YOU WIN!!")
                else:
                    print("YOU LOSE!!")
                    win = 1
                opened = True
            else:
                a, b = input("Enter two values: ").split()
                num = int(a)
                val = int(b)
                while(not check(current, num, val)):
                    a, b = input("Enter two values again: ").split()
                    num = int(a)
                    val = int(b)
                    
                if num <= 5:
                    if(val > 1 and val < 6):
                        current = [num, val + 1]
                        print("Computer's move: ", num, val + 1)
                    else:
                        current = [num + 1, val]
                        print("Computer's move: ", num + 1, val)
                else:
                    print("Computer opens the cup!")
                    
                    if open(d1, d2, num, val):
                        print("YOU LOSE!!")
                        win = 1
                    else:
                        print("YOU WIN!!")
                    opened = True
                count += 1
        if win == 0:
            winner = "User"
        else:
            winner = "AI"
        d1String = ','.join(str(d) for d in d1)
        d2String = ','.join(str(d) for d in d2)
        populate_table.populate(d1String, d2String, winner)

        
        print(d1)
        print(d2)
        counter += 1
