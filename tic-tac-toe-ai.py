import os
clear = lambda: os.system('cls') # Clears the console.

# Ask the user for a postion and return its board coordinates
def getHumanMove():
    move = -1
    while move == -1:
        move = input("Human's Turn: ")
        try:
            move = int(move)
        except ValueError:
            print("Please enter a number between 1 and 9")
            move = -1
    
    positions = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2]
    }

    return positions.get(move)
    
# Update the game board    
def updateBoard(player, position):
    board[position[1]][position[0]] = player

# Display the board
def displayBoard():
    b = board
    for i in range(3):
        for j in range(3):
            if b[i][j] == 1:
                b[i][j] = 'x'
            elif b[i][j] == -1:
                b[i][j] = 'o'
            else:
                b[i][j] = ' '

    print("-------------")
    print("| " + b[0][0] + " | " + b[0][1] + " | " + b[0][2] + " | ")
    print("-------------")
    print("| " + b[1][0] + " | " + b[1][1] + " | " + b[1][2] + " | ")
    print("-------------")
    print("| " + b[2][0] + " | " + b[2][1] + " | " + b[2][2] + " | ")
    print("-------------")

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

    if [1, 1, 1] in winningCombinations:
        return 1 # Human won
    elif [-1, -1, -1] in winningCombinations:
        return -1 # AI won
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    return 2 # There are more spaces to fill 
        return 0 # Tie

# Game Board
board = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

# Players
human = 1
ai = -1

# Start Game
clear()
