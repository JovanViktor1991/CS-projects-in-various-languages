"""
Author: Viktor Jovanovic

File: AI_TwiddleBoard.py

Description: Twiddle board, a program that finds solution to a nine integer input.
"""

"""Breadth First Search"""


from collections import deque

explored = {}
frontier = deque()
moves = {0:"aC", 1:"aCC", 2:"bC", 3:"bCC",4:"cc",5:"cCC", 6:"dC",7:"dCC"}

def getBoardConfig():
    """getBoardConfig represents each of the
8 possible moves (4 rotation points x 2 rotation directions"""
    
    field = [board, 0, 0] #my current state

    frontier.append(field)

    return board

def search(board = " "):
    global frontier
    global explored

    frontier = deque()
    explored = {}

    if board == " ":
        board = input("Search: ")
    else:
        board = str(board) #string used to represent the moves we are making

    frontier.append((board, "")) #number of things wating for you

    goal = "123456789"
    counter = 0

    while len(frontier) > 0:
        temp = frontier.popleft()#pop left
        counter += 1
        if temp[0] == goal:
            break
        if temp[0] not in explored: #refers to temp which is a tuple
            explored[temp[0]] = 0 #contains the number of boards I looked at
            generateChildren(temp[0], temp[1])#sends in string of 9

    print("This board can be solved by doing\n", temp[1])
    print("Consider a total of " + str(counter) + " boards")
    print("Fringe still contains " + str(len(frontier))+ " boards")
        
def generateChildren(next1, movesSoFar):
    """generateChildrn() generates all the children of the parent node and appends them to the
frontier"""

    frontier.append((next1[3] + next1[0] + next1[2] + next1[4] + next1[1] + next1[5:9], movesSoFar + " aC "))#clockwise a
    frontier.append((next1[1] + next1[4] + next1[2] + next1[0] + next1[3] + next1[5:9], movesSoFar + " aCC "))#counter clockwise a
    frontier.append((next1[0] + next1[4] + next1[1] + next1[3] + next1[5] + next1[2] + next1[6:9], movesSoFar + " bC "))#clockwise b
    frontier.append((next1[0] + next1[2] + next1[5] + next1[3] + next1[1] + next1[4] + next1[6:9], movesSoFar + " bCC "))#Counter Clockwise b
    frontier.append((next1[0:3] + next1[6] + next1[3] + next1[5] + next1[7] + next1[4] + next1[8], movesSoFar + " cC "))#clockwise c
    frontier.append((next1[0:3] + next1[4] + next1[7] + next1[5] + next1[3] + next1[6] + next1[8], movesSoFar + " cCC "))#counter clockwise c
    frontier.append((next1[0:4] + next1[7] + next1[4] + next1[6] + next1[8] + next1[5], movesSoFar + " dC "))#clockwise d
    frontier.append((next1[0:4] + next1[5] + next1[8] + next1[6] + next1[4] + next1[7], movesSoFar + " dCC "))#counter clockwise d
    
#import cProfile, used to tell me what parts of my code were taking the most, in my case it was pop. Before edits, code took 10 minutes 
#cProfile.run('search()')   
        
