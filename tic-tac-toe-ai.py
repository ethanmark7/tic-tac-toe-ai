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

# Game Board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Players
human = 1
ai = -1


clear()
updateBoard(human, [1, 2])
print(board)