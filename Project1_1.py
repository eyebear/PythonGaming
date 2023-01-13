import random
import os
'''
Task on 20230113
1. user can set the mapsize
2. add boundary conditioncheck to filter invalid moves
3. put together monster check and winning check, and portal warp etc. in condition check
4. add portal
5. add helicopter
'''

#feature1: set the map size
size = int(input("Enter your map size: "))
gameWon = False
metMonster = False
gameMap = [['+'] * size for r in range(size)]
playerPos = [0, 0]


def printMap():
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(size):
    string = ""
    for j in range(len(gameMap[i])):
      string += gameMap[i][j]
    print(string)
  print("~~~~~~~~")


def generateRandomPos(size):
  rand2 = random.randint(0, (size - 1))
  rand3 = random.randint(0, (size - 1))
  return rand2, rand3


def resetGame():
  #player
  gameMap[playerPos[0]][playerPos[1]] = 'P'
  #gold
  gameMap[size - 1][size - 1] = 'G'

  #generate monsters and one portal
  rand1 = random.randint(size // 2, size)
  portalSet = False
  chopperSet = False
  for i in range(rand1):
    randY, randX = generateRandomPos(size)
    #feature 4 add portal
    if gameMap[randY][randX] == '+' and not portalSet:
      gameMap[randY][randX] = 'O'
      portalSet = True
    if gameMap[randY][randX] == '+' and not chopperSet:
      gameMap[randY][randX] = 'H'
      chopperSet = True
    if gameMap[randY][randX] == '+':
      gameMap[randY][randX] = 'M'

  printMap()


def moveLeft():
  gameMap[playerPos[0]][playerPos[1]] = '+'
  playerPos[1] -= 1
  conditionCheck()
  gameMap[playerPos[0]][playerPos[1]] = 'P'
  printMap()


def moveRight():
  gameMap[playerPos[0]][playerPos[1]] = '+'
  playerPos[1] += 1
  conditionCheck()
  gameMap[playerPos[0]][playerPos[1]] = 'P'
  printMap()


def moveUp():
  gameMap[playerPos[0]][playerPos[1]] = '+'
  playerPos[0] -= 1
  conditionCheck()
  gameMap[playerPos[0]][playerPos[1]] = 'P'
  printMap()


def moveDown():
  gameMap[playerPos[0]][playerPos[1]] = '+'
  playerPos[0] += 1
  conditionCheck()
  gameMap[playerPos[0]][playerPos[1]] = 'P'
  printMap()


#feature  3: conditioncheck
def conditionCheck():
  if gameMap[playerPos[0]][playerPos[1]] == 'M':
    global metMonster
    metMonster = True
  if gameMap[playerPos[0]][playerPos[1]] == "G":
    global gameWon
    gameWon = True
  #feature 4: portal check
  if gameMap[playerPos[0]][playerPos[1]] == "O":
    playerPos[0], playerPos[1] = generateRandomPos(size)
    printMap
    conditionCheck()
  #feature 5: chopper
  if gameMap[playerPos[0]][playerPos[1]] == "H":
    #assume all valid move
    playerPos[0], playerPos[1] = map(
      int,
      input("Enter a pair of X and Y location: ").split())
    conditionCheck()
    print(playerPos[0], playerPos[1])


#feature 2: valid move check
def isValidMove(cmd):
  if cmd == 'w' and playerPos[0] - 1 >= 0:
    return True
  elif cmd == 's' and playerPos[0] + 1 <= size - 1:
    return True
  elif cmd == 'a' and playerPos[1] - 1 >= 0:
    return True
  elif cmd == 'd' and playerPos[1] + 1 <= size - 1:
    return True
  else:
    return False


def play():
  resetGame()
  while True:
    cmd = input("Enter Command wasd to move or x to quit: ")
    if cmd == "X":
      break
    if cmd == "w" and isValidMove(cmd):
      moveUp()
    elif cmd == "a" and isValidMove(cmd):
      moveLeft()
    elif cmd == "s" and isValidMove(cmd):
      moveDown()
    elif cmd == "d" and isValidMove(cmd):
      moveRight()
    else:
      printMap()
      print("invalid input")

    if gameWon:
      print("You have found the gold!")
      break
    if metMonster:
      #feature 5: if meet monster, show X to indivate death
      gameMap[playerPos[0]][playerPos[1]] = 'X'
      printMap()
      print("You just met a monster, your player died.")
      break


play()
