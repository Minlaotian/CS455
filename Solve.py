from RubiksCube import PrintCube, scrambleCube,  rotations
import numpy as np
from datetime import datetime
import time


# State class that for every state of the cube
# Depth is based on how many turns is needed to get from the initial state to the node
# Cube will initially be filled with a solved cube
class State:
    depth = 0
    parent = None
    cube = [[' ' for _ in range(12)] for _ in range(9)]
    cube = np.array(cube)
    colors = ('W', 'O', 'G', 'R', 'B', 'Y')

    for row in range(3):
        for column in range(3, 6):
            cube[row][column] = colors[0]

    for row in range(3, 6):
        for column in range(3):
            cube[row][column] = colors[1]

        for column in range(3, 6):
            cube[row][column] = colors[2]

        for column in range(6, 9):
            cube[row][column] = colors[3]

        for column in range(9, 12):
            cube[row][column] = colors[4]

    for row in range(6, 9):
        for column in range(3, 6):
            cube[row][column] = colors[5]


# Creates a new cube in a solved state
# and will compare the current state with the solved state
# If it returns true, break out of the loops in IDFSAlgorithm
def SolvedCube(self):
    solvedState = [[' ' for _ in range(12)] for _ in range(9)]
    solvedState = np.array(solvedState)
    colors = ('W', 'O', 'G', 'R', 'B', 'Y')

    for row in range(3):
        for column in range(3, 6):
            solvedState[row][column] = colors[0]

    for row in range(3, 6):
        for column in range(3):
            solvedState[row][column] = colors[1]

        for column in range(3, 6):
            solvedState[row][column] = colors[2]

        for column in range(6, 9):
            solvedState[row][column] = colors[3]

        for column in range(9, 12):
            solvedState[row][column] = colors[4]

    for row in range(6, 9):
        for column in range(3, 6):
            solvedState[row][column] = colors[5]

    if (self == solvedState).all():
        print("Solution Found!")
        return True
    else:
        return False


# Checks if the current node is the same as the parent node
def ChildIsInParent(child, parent):
    currentState = parent.parent
    while currentState is not None:
        if np.array_equal(currentState.cube, child):
            return True
        currentState = currentState.parent
    return False


# Checks if the current node is the same as any of the parent nodes
def ChildIsInFrontier(child, frontier):
    for current in frontier:
        if np.array_equal(current.cube, child):
            return True
        else:
            return False


# Main Algorithm Loop
def IDFSAlgorithm(self):
    rotationList = ['R', 'L', 'D', 'U', 'F', 'B', 'RPRIME', 'LPRIME', 'UPRIME', 'DPRIME', 'FPRIME', 'BPRIME']
    depthBound = 1
    nodes = 0
    frontier = list()

    # Starts the whole process with the initial scrambled state
    while True:
        frontier.append(self)

        while len(frontier) != 0:
            currentState = frontier.pop()

            # Breaks out of the loops and prints values
            if SolvedCube(currentState.cube):
                print('Depth for the Goal:', currentState.depth)
                print("Number of Nodes Created:", nodes)
                return

            # Goes to the next depth
            if currentState.depth + 1 <= depthBound:
                childDepth = currentState.depth + 1

                # Creates a new Cube node that will contain the next move in a depth further down
                # Checks if that node has been created before
                # If it's a new node then append it to the frontier for checking if solved
                for i in rotationList:
                    nodes = nodes + 1
                    new = State()
                    new.cube = np.array(currentState.cube)
                    new.depth = childDepth
                    new.parent = currentState
                    rotations(new.cube, i)

                    if currentState.parent is not None and (ChildIsInParent(new.cube, currentState) or ChildIsInFrontier(new.cube, frontier)):
                        continue
                    frontier.append(new)

        # Allows the next iteration go into a further depth
        depthBound = depthBound + 1

##################################################


# Creates a new cube that will be scrambled and solved in the Algorithm
newCube = State()
scrambleCube(newCube.cube, 5)
print('\n\tThe Scramble Is')
PrintCube(newCube.cube)
print()

# Starts a timer to see how long it will take to solve
time.ctime()
fmt = '%H:%M:%S'
start = time.strftime(fmt)

IDFSAlgorithm(newCube)

# Ends and displays time once the cube is solved
time.ctime()
end = time.strftime(fmt)
print("Time taken(sec):", datetime.strptime(end, fmt) - datetime.strptime(start, fmt))