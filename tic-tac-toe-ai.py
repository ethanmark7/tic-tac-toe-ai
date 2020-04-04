import os
import copy
import time
from math import inf as infinity

# Clear console func
clear = lambda: os.system('cls') 

# Game Board
board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

# Players
human = 1
ai = -1


# Ask the user for a postion and return its board coordinates
def getHumanMove():
    move = -1
    positions = {
        1: [0, 0], 2: [1, 0], 3: [2, 0],
        4: [0, 1], 5: [1, 1], 6: [2, 1],
        7: [0, 2], 8: [1, 2], 9: [2, 2]
    }

    while move == -1 or move > 9 or move < 1:
        move = input("Human's Turn: ")
        try:
            move = int(move)
            if move < 9 and move > 1:
                if board[positions.get(move)[1]][positions.get(move)[0]] != 0:
                    print("Someone else occupies that space...")
                    move = -1
        except ValueError:
            print("Please enter a number between 1 and 9")
            move = -1

    return positions.get(move)
    
# Update the game board    
def updateBoard(player, position): 
    board[position[1]][position[0]] = player

# Display the board
def displayBoard():
    b = copy.deepcopy(board)

    for i in range(3):
        for j in range(3):
            if b[i][j] == ai:
                b[i][j] = 'o'
            elif b[i][j] == human:
                b[i][j] = 'x'
            else:
                b[i][j] = ' '

    print("-------------")
    print("| " + b[0][0] + " | " + b[0][1] + " | " + b[0][2] + " | ")
    print("-------------")
    print("| " + b[1][0] + " | " + b[1][1] + " | " + b[1][2] + " | ")
    print("-------------")
    print("| " + b[2][0] + " | " + b[2][1] + " | " + b[2][2] + " | ")
    print("-------------")

# Return empty cells
def emptyCells():
    emptyCells = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                emptyCells += 1

    return emptyCells

def checkForWinner():
    winningCombinations = [
        [board[0][0], board[0][1], board[0][2]], # Horizontals
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]], # Verticals
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]], # Diagonals
        [board[2][0], board[1][1], board[0][2]],
    ]

    if [ai, ai, ai] in winningCombinations:
        return 1 # Human won
    elif [human, human, human] in winningCombinations:
        return -1 # AI won
    else:
        if emptyCells() == 0:
            return 0
        else:
            return 2

def humanTurn():
    updateBoard(human, getHumanMove())
    displayBoard()

paths = []

def minimax(depth, player): 
    if player == ai:
        maxVal = [-1, -1, -infinity]
    else:
        maxVal = [-1, -1, +infinity]

    if depth == 0 or checkForWinner() != 2:
        return[-1, -1, checkForWinner()]

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player  
                score = minimax(depth - 1, -player)
                board[i][j] = 0
                
                if player == ai:
                    if score[2] > maxVal[2]:
                        maxVal = score
                        maxVal[0], maxVal[1] = i, j
                else:
                    if score[2] < maxVal[2]:
                        maxVal = score
                        maxVal[0], maxVal[1] = i, j

    return maxVal

def aiTurn():
    pos = minimax(emptyCells(), ai)
    updateBoard(ai, [pos[1], pos[0]])
    clear()
    displayBoard()

# Manages the board
def main():
    clear() # Clear the console

    print("Welcome Human!")
    displayBoard()

    while checkForWinner() == 2:
        
        humanTurn()

        # Loading animation
        for x in range(4):  
            b = "Thinking" + "." * x
            print (b, end="\r")
            time.sleep(0.25)

        aiTurn()

    if checkForWinner() == human:
        print("Honestly dude, you had no chance! RIP")
    elif checkForWinner() == ai:
        print("You will never see this secret message.")
    else:
        print("Good try, maybe next time you'll win. ;)")

main()