import numpy
import random
import math
from scipy.special import binom, factorial

#MYSQL import
''' import DBHelper.ResultTable.gen_res_tb as resGen
import DBHelper.ResultTable.ins_res_tb as resIns '''

class database():
    def __init__(self):
        self.data = []
        self.total = total()

    def createGame(self, calls):
        result = []
        for call in calls:
            result.append(call)
        self.data.append(call)

    def createCall(self, who, diceNum, dicePoint):
        return who, diceNum, dicePoint

def bluff(call, playerDice):
    numCount = 0
    for i in playerDice:
        if i == call[2] or i == 1:
            numCount += 1
    if call[1] >= 6:
        return numCount < call[1] / 2.0 + 1
    else:
        return numCount < call[1] / 2.0

def callBluff(call, playerDice):
    numCount = 0
    for i in playerDice:
        if i == call[2] or i == 1:
            numCount += 1
    return numCount < call[1] / 3.0

class total():
    def __init__(self):
        self.start = [1, 2]
        self.add = [1, 2]
        self.switch = [1, 2]
        self.call = [1, 2]

    def printData(self):
        print(str(self.start[0]), str(self.start[1]))
        print(str(self.add[0]), str(self.add[1]))
        print(str(self.switch[0]), str(self.switch[1]))
        print(str(self.call[0]), str(self.call[1]))

    def updateStart(self, game, playerDice):
        if game[0][0] == 1:
            if bluff(game[0], playerDice):
                self.start[0] += 1
                self.start[1] += 1
            else:
                self.start[1] += 1

    def updateAdd(self, game, playerDice):
        for i in range(2, len(game)):
            if game[i][0] == 1:
                if game[i][2] == game[i - 2][2]:
                    if bluff(game[i], playerDice):
                        self.add[0] += 1
                        self.add[1] += 1
                    else:
                        self.add[1] += 1

    def updateSwitch(self, game, playerDice):
        for i in range(1, len(game)):
            if i == 1:
                if game[1][0] == 1:
                    if game[1][2] != game[0][2]:
                        if bluff(game[1], playerDice):
                            self.add[0] += 1
                            self.add[1] += 1
                        else:
                            self.add[1] += 1
            else:
                if game[i][0] == 1:
                    if game[i][2] != game[i - 2][2] and game[i][2] != game[i - 1][2]:
                        if bluff(game[i], playerDice):
                            self.add[0] += 1
                            self.add[1] += 1
                        else:
                            self.add[1] += 1

    def updateCall(self, game, playerDice):
        for i in range(1, len(game)):
            if i == 1:
                print(game)
                if game[1][0] == 1:
                    if game[1][2] == game[0][2]:
                        if callBluff(game[i], playerDice):
                            self.add[0] += 1
                            self.add[1] += 1
                        else:
                            self.add[1] += 1
            else:
                if game[i][0] == 1:
                    if game[i][2] != game[i - 2][2] and game[i][2] == game[i - 1][2]:
                        if callBluff(game[i], playerDice):
                            self.call[0] += 1
                            self.call[1] += 1
                        else:
                            self.call[1] += 1

    def updateAll(self, game, playerDice):
        self.updateStart(game, playerDice)
        self.updateAdd(game, playerDice)
        self.updateCall(game, playerDice)
        self.updateSwitch(game, playerDice)

    def getStartBluff(self):
        return self.start[0] / (self.start[1])

    def getAddBluff(self):
        return self.add[0] / (self.add[1])

    def getSwitchBluff(self):
        return self.switch[0] / (self.switch[1])

    def getCallBluff(self):
        return self.call[0] / (self.call[1])

    def printing(self):
        print(self.add)
        print(self.switch)
        print(self.call)
        print(self.start)

def open(d1, d2, call):
    n = call[1]
    k = call[2]
    count = 0
    for x in range(0, 5):
        if (d1[x] == k or d1[x] == 1):
            count += 1
        if (d2[x] == k or d2[x] == 1):
            count += 1
    if set(d1) == {1} or set(d1) == {k} or set(d1) == {1, k}:
        count += 1
    if set(d2) == {1} or set(d2) == {k} or set(d2) == {1, k}:
        count += 1
    return count >= n

def check(call, n, k):
    if n not in range(3, 14) or k not in range(2, 7):
        print("Out of range or wrong type of data.")
        return False
    elif call[1] > n:
        print("The number must be larger or equal the one in the previous round.")
        return False
    elif call[1] == n and call[2] >= k:
        print("The value must be larger than the one in the previous round if the number keeps the same.")
        return False
    return True

def count(d2):
    counting = []
    for x in range(5):
        counting.append(d2.count(x + 2) + d2.count(1))
    return counting

def has4(d2):
    countList = count(d2)
    most = max(countList)
    if most >= 4:
        return countList.index(most) + 2
    else:
        return 0

def reverse(countList):
    counting = count(countList)
    counting.reverse()
    return counting

def switch(call, computerList):
    n = call[1]
    k = call[2]
    if n == 3 and k < 6:
        k1 = first_move(call, computerList)
        return (0, n, k1)
    elif n == 3 and k == 6:
        return (0, 4, random.choice([2, 3, 4, 5]))
    elif n == 4 and k < 6:
        return (0, 4, random.choice(list(range(k + 1, 7))))
    else:
        reversed = reverse(computerList)
        val = 6 - reversed.index(max(reversed))
        if max(reversed) >= 3 and (n == 4 or (n == 5 and val > k)):
            return (0, 5, val)
        return (2, n, k)

def first_move(call, computerList):
    k = call[2]
    if 1 in computerList:
        counting = count(computerList)
        for x in range(k - 1):
            counting.pop(0)
        print(counting)
        return counting.index(min(counting)) + k + 1
    missing = list(set(range(2, 7)) - set(computerList))
    if (len(missing)) >= 1 and random.random() <= 0.7 and missing[0] > k:
        return missing[0]
    return random.choice(list(range(k + 1, 7)))

# type-computer start = -1 after switch = 1, after call = 2, after add = 3, after start = 4
def play(type, d2, game, total, call):
    num = has4(d2)
    if num > 0 and call[2] < num:
        return 0, call[1], num
    elif num > 0:
        return 0, call[1] + 1, num
    elif type == -1:
        return 0, 3, first_move(d2)
    else:
        playerCall = game[len(game) - 1]
        if type == 4:
            bluff = random.random() < total.getSwitchBluff()
        if type == 3:
            bluff = random.random() < total.getCallBluff()
        if type == 2:
            bluff = random.random() < total.getAddBluff()
        if type == 1:
            bluff = random.random() < total.getStartBluff()
        if bluff:
            playerCount = math.ceil(playerCall[1] / 2.0) - 1
        else:
            playerCount = math.ceil(playerCall[1] / 2.0)
        myCount = 0
        for i in d2:
            if i == playerCall[2] or i == 1:
                myCount += 1
        if myCount + playerCount < playerCall[1] - 1:
            return (2, call[1], call[2])
        elif myCount + playerCount < playerCall[1]:
            if random.random() < 0.3:
                return switch(call, d2)
            return (2, call[1], call[2])
        elif myCount + playerCount > playerCall[1]:
            return 0, playerCall[1] + 1, playerCall[2]
        else:
            if random.random() < 0.3:
                return (2, call[1], call[2])
            return switch(call, d2)

def callType(gameList):
    if len(gameList) == 0:
        return -1
    elif len(gameList) == 1:
        return 1
    elif (gameList[len(gameList) - 1][2] == gameList[len(gameList) - 3][2]):
        return 2
    elif (gameList[len(gameList) - 1][2] == gameList[len(gameList) - 2][2]
          and gameList[len(gameList) - 1][2] != gameList[len(gameList) - 3][2]):
        return 4
    else:
        return 3

if __name__ == '__main__':

    #MYSQL gen table
    ''' gen = resGen.gen_res_tb() '''

    data = database()
    total = total()
    print("Welcome to the BAR DICE!")
    rounds = int(input("How any rounds would you like to play?"))
    stats = 0.0
    counter = 0
    while rounds not in range(3, 11):
        rounds = int(input("INVALID INPUT. Out of range or wrong type of data. Try again: "))
    if rounds in range(3, 11):
        print("Challenge accepted! I will play you for", rounds, "rounds! Let's begin!!!")

    while counter <= rounds - 1:
        call = (0, 0, 0)
        opened = False
        round = 0
        d1 = []
        d2 = []

        #MYSQL return var
        ''' winner = "" '''

        while len(set(d1)) == len(d1):
            d1 = []
            for i in range(0, 5):
                n = random.randint(1, 6)
                d1.append(n)

        while len(set(d2)) == len(d2):
            d2 = []
            for i in range(0, 5):
                n = random.randint(1, 6)
                d2.append(n)
    
        print("YOUR DICE: ", d1)
        gameList = []
        
        while not opened:
            if (round > 0) and input("Do you want to open? y/n") == "y":
                if open(d1, d2, call):
                    print("YOU LOSE!")
                else:
                    stats += 1
                    print("YOU WIN!")
                opened = True
            else:
                a, b = input("Enter two values: ").split()
                num = int(a)
                val = int(b)

                while not check(call, num, val):
                    a, b = input("Enter two values again: ").split()
                    num = int(a)
                    val = int(b)
                call = (1, num, val)
                gameList.append(call)
                call = play(callType(gameList), d2, gameList, total, call)
                if call[0] == 2:
                    if open(d1, d2, call):
                        stats += 1
                        print("YOU WIN!")
                    else:
                        print("YOU LOSE!")
                    opened = True

                    #MYSQL insert
                    ''' d1String = ','.join(str(d) for d in d1)
                    d2String = ','.join(str(d) for d in d2)
                    resIns.ins_res_tb(d1String, d2String, winner) '''

                    print("game over: opened")
                else:
                    print(call)
                    gameList.append(call)
                round += 1

        data.data.append(gameList)
        total.updateAll(gameList, d1)
        print(d1)
        print(d2)
        counter += 1
    print("Player:", stats)
    print("AI:", rounds - stats)
    total.printData()
