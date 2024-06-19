
import random
from random import randint
from re import sub
import sys

def createGamba():
    GambaList = [0] * 2
    GambaList[0] = {}
    GambaList[0] = random.sample(range(1,69), 5)

    GambaList[1] = randint(1,26)
    GambaList[0].sort()
    return GambaList

def check(List1, List2):
    set1 = set(List1)
    set2 = set(List2)
    common = set1.intersection(set2)
    return len(common)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def amountInput():
    while True:
        amount = input("Ticket Amount\n")

        if amount == "exit":
            sys.exit(0)
        elif is_integer(amount):
            return amount
        else:
            print("Not a number")

def gambaInput(strInput):
    while True:
            Gamba = input(strInput)
            if Gamba == "exit":
                sys.exit(0)
            elif Gamba.lower() == 'yes':
                return 1
            elif Gamba.lower() == 'no':
                return 0
            else:
                print("Yes or No")

amount = 0
MoneySpent = 0
MoneyWon = 0
MoneyProfit = 0
GambaPlay = 0
totalWinnings = 0
BaseNumbers = createGamba()

print(BaseNumbers)

GrandPrize = 56_000_000

print("Grand Prize: ", GrandPrize)
while True:
    amount = amountInput()
    GambaBall = gambaInput("Gamba Ball?\n")
    GambaPlay = gambaInput("Gamba Play?\n")

    MoneySpent = MoneySpent + ((GambaPlay + GambaBall + 2) * int(amount))
    currentWinningsList = []
    for x in range(int(amount)):
        subject = createGamba()
        #print(subject)
        commons = check(BaseNumbers[0], subject[0])
        GambaBallMatch = False
        if GambaBall:
            GambaBallMatch = BaseNumbers[1] == subject[1]

        GambaMultiplier = 1
        if GambaPlay:
            if GrandPrize < 150_000_000:
                GambaMultiplier = randint(1, 43)
            else:
                GambaMultiplier = randint(1, 42)

        # if GambaMultiplier in range(1,24):
        #     GambaMultiplier = 2
        # elif GambaMultiplier in range(23, 36):
        #     GambaMultiplier = 3
        # elif GambaMultiplier in range(37, 40):
        #     GambaMultiplier = 4
        # elif GambaMultiplier in range(41, 42):
        #     GambaMultiplier = 5
        # elif GambaMultiplier == 43:
        #     GambaMultiplier = 10

        ranges = [
        (range(1 , 24), 2),  # 24 balls
        (range(23, 36), 3), # 13 balls
        (range(37, 40), 4), # 3 balls
        (range(41, 42), 5), # 2 balls
        (range(43, 44), 10) # 1 ball # Adjusted range to include 43
        ]

        for r, multiplier in ranges:
            if GambaMultiplier in r:
                GambaMultiplier = multiplier
                break

        # tempWinnings = 0
        # if commons == 0:
        #     if GambaMatch:
        #         tempWinnings = 4
        #     else:
        #         tempWinnings = 0
        # elif commons == 1:
        #     if GambaMatch:
        #         tempWinnings = 4
        #     else:
        #         tempWinnings = 0
        # elif commons == 2:
        #     if GambaMatch:
        #         tempWinnings = 7
        #     else:
        #         tempWinnings = 0
        # elif commons == 3:
        #     if GambaMatch:
        #         tempWinnings = 100
        #     else:
        #         tempWinnings = 7
        # elif commons == 4:
        #     if GambaMatch:
        #         tempWinnings = 50_000
        #     else:
        #         tempWinnings = 100
        # elif commons == 5:
        #     if GambaMatch:
        #         tempWinnings = 56_000_000
        #     else:
        #         tempWinnings = 1_000_000

        # Define the winnings based on commons and GambaMatch
        winnings_map = {
            0: (0, 4),  # (winnings if no match, winnings if match)
            1: (0, 4),
            2: (0, 7),
            3: (7, 100),
            4: (100, 50_000),
            5: (1_000_000, 56_000_000)
        }

        # Assign tempWinnings based on commons and GambaMatch
        if commons in winnings_map:
            no_match, match = winnings_map[commons]
            tempWinnings = match if GambaBallMatch else no_match
        else:
            tempWinnings = 0  # Default case if commons is not in the map


        if commons == 5 and GambaPlay:
            if GambaBall:
                currentWinningsList.append(GrandPrize)
            else:
                currentWinningsList.append(2_000_000)
        else:
            currentWinningsList.append(tempWinnings * GambaMultiplier)

    totalWinnings = totalWinnings + sum(currentWinningsList)
    print(currentWinningsList)
    print("Current Winnings", sum(currentWinningsList))
    print("Money Spent", MoneySpent)
    print("Total Winnings", totalWinnings)
    print("Profit", totalWinnings - MoneySpent)


    #Fix PowerPlay (+1 cost not doubling rewards)