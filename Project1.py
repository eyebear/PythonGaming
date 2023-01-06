import random
import os

gameMap = [['+']*8 for r in range(8)]
playerPos = [0,0]
def printMap():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(8):
        string = ""
        for j in range(len(gameMap[i])):
            string += gameMap[i][j]
        print(string)
    print("~~~~~~~~")


def resetGame():
    #player
    gameMap[playerPos[0]][playerPos[1]] = 'P'
    #gold
    gameMap[7][7] = 'G'
    rand1 = random.randint(5,20)
    for i in range(rand1):
        rand2 = random.randint(0, 7)
        rand3 = random.randint(0, 7)
        if gameMap[rand2][rand3] == '+':
            gameMap[rand2][rand3] = 'M'
    printMap()

def moveLeft():
    gameMap[playerPos[0]][playerPos[1]] = '+'
    playerPos[1] -= 1
    monsterCheck()
    gameMap[playerPos[0]][playerPos[1]] = 'P'
    printMap()
def moveRight():
    gameMap[playerPos[0]][playerPos[1]] = '+'
    playerPos[1] += 1
    monsterCheck()
    gameMap[playerPos[0]][playerPos[1]] = 'P'
    printMap()
def moveUp():
    gameMap[playerPos[0]][playerPos[1]] = '+'
    playerPos[0] -= 1
    monsterCheck()
    gameMap[playerPos[0]][playerPos[1]] = 'P'
    printMap()
def moveDown():
    gameMap[playerPos[0]][playerPos[1]] = '+'
    playerPos[0] += 1
    monsterCheck()
    gameMap[playerPos[0]][playerPos[1]] = 'P'
    printMap()

def monsterCheck():
    if gameMap[playerPos[0]][playerPos[1]] == 'M':
      print("You met a monster. Your player died")
      exit()

def play():
    resetGame()
    cmd = input("Enter Command wasd to move or x to quit: ")
    while cmd !="X":
        if cmd == "w":
            moveUp()
        elif cmd == "a":
            moveLeft()
        elif cmd == "s":
            moveDown()
        elif cmd == "d":
            moveRight()
        else:
            print("invalid input")
        if playerPos[0] == 7 and playerPos[1]==7:
            print("You have found the gold!")
            break
        cmd = input("Enter Command wasd to move or x to quit: ")

play()









