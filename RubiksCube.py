import numpy as np
import random


def PrintCube(self):
    print('_ _ _ ', self[0, 3], self[0, 4], self[0, 5], ' _ _ _  _ _ _')
    print('_ _ _ ', self[1, 3], self[1, 4], self[1, 5], ' _ _ _  _ _ _')
    print('_ _ _ ', self[2, 3], self[2, 4], self[2, 5], ' _ _ _  _ _ _')

    print(self[3, 0], self[3, 1], self[3, 2], '', self[3, 3], self[3, 4], self[3, 5],
          '', self[3, 6], self[3, 7], self[3, 8], '', self[3, 9], self[3, 10], self[3, 11])

    print(self[4, 0], self[4, 1], self[4, 2], '', self[4, 3], self[4, 4], self[4, 5],
          '', self[4, 6], self[4, 7], self[4, 8], '', self[4, 9], self[4, 10], self[4, 11])

    print(self[5, 0], self[5, 1], self[5, 2], '', self[5, 3], self[5, 4], self[5, 5],
          '', self[5, 6], self[5, 7], self[5, 8], '', self[5, 9], self[5, 10], self[5, 11])

    print('_ _ _ ', self[6, 3], self[6, 4], self[6, 5], ' _ _ _  _ _ _')
    print('_ _ _ ', self[7, 3], self[7, 4], self[7, 5], ' _ _ _  _ _ _')
    print('_ _ _ ', self[8, 3], self[8, 4], self[8, 5], ' _ _ _  _ _ _')


def scrambleCube(self, moves):
    for i in range(moves):
        option = random.randint(0, 11)

        if option == 0:
            rotations(self, 'R')
        if option == 1:
            rotations(self, 'L')
        if option == 2:
            rotations(self, 'U')
        if option == 3:
            rotations(self, 'D')
        if option == 4:
            rotations(self, 'F')
        if option == 5:
            rotations(self, 'B')
        if option == 6:
            rotations(self, 'RPRIME')
        if option == 7:
            rotations(self, 'LPRIME')
        if option == 8:
            rotations(self, 'UPRIME')
        if option == 9:
            rotations(self, 'DPRIME')
        if option == 10:
            rotations(self, 'FPRIME')
        if option == 11:
            rotations(self, 'BPRIME')


def rotations(self, move):
    turnList = ['R', 'L', 'U', 'D', 'F', 'B', 'RPRIME', 'LPRIME', 'UPRIME', 'DPRIME', 'FPRIME', 'BPRIME']

    if move not in turnList:
        raise ValueError("valid moves are 'R', 'L', 'U', 'D', 'F', 'B' and their prime counterparts")

    if move == 'R':
        # temp array to store the list of the values being moved
        temp = []

        # Moving the Right face in any direction requires the values
        # at column 5 and the values at column 9
        column = 5
        otherColumn = 14 - column

        # Any value moving between column and otherColumn must be flipped

        # Assigns three values at Column 5 to temp and then flips it
        temp[0:3] = [self[row][column] for row in range(3)]
        temp[0:3] = np.flip(temp[0:3])

        # Assigns the other six values at Column 5 to temp No need to flip
        temp[3:9] = [self[row][column] for row in range(3, 9)]

        # Assigns the otherColumn's three values at Column 9 to temp and then flips it
        temp[9:12] = [self[row][otherColumn] for row in range(3, 6)]
        temp[9:12] = np.flip(temp[9:12])

        # Reorders the list to place them back into self
        temp = temp[3:] + temp[:3]

        # Places the temp values back into self
        for row in range(9):
            self[row][column] = temp[row]

        for row in range(3, 6):
            self[row][otherColumn] = temp[row + 6]

        # Moving the Right face also rotates the Right side
        # Since np.rot rotates counter clockwise, k must be three to simulate
        # a clockwise turn.
        self[3:6, 6:9] = np.rot90(self[3:6, 6:9], k = 3)

    if move == 'L':
        # temp array to store the list of the values being moved
        temp = []

        # Moving the Left face in any direction requires the values
        # at column 5 and the values at column 9
        column = 3
        otherColumn = 14 - column

        # Any value moving between column and otherColumn must be flipped

        # Assigns three values at Column 5 to temp and then flips it
        temp[0:6] = [self[row][column] for row in range(3)]

        # Assigns the other six values at Column 5 to temp No need to flip
        temp[6:9] = [self[row][column] for row in range(3, 9)]
        temp[6:9] = np.flip(temp[6:9])

        # Assigns the otherColumn's three values at Column 9 to temp and then flips it
        temp[9:12] = [self[row][otherColumn] for row in range(3, 6)]
        temp[9:12] = np.flip(temp[9:12])

        # Reorders the list to place them back into self
        temp = temp[-3:] + temp[:-3]

        # Places the temp values back into self
        for row in range(9):
            self[row][column] = temp[row]

        for row in range(3, 6):
            self[row][otherColumn] = temp[row + 6]

        # Moving the Left face also rotates the Left side
        # Since np.rot rotates counter clockwise, k must be three to simulate
        # a clockwise turn.
        self[3:6, 0:3] = np.rot90(self[3:6, 0:3], k=3)

    if move == 'U':
        # Works in the third row to rotate the Top face
        row = 3
        # Column set to three to swap everything after the first three columns
        # with the values at the first three columns
        column = 3

        # Swaps the values stated above
        self[row, :] = np.concatenate((self[row, column:], self[row, :column]))

        # Rotates the top face
        self[0:3, 3:6] = np.rot90(self[0:3, 3:6], k=3)

    if move == 'D':
        # Works in the third row to rotate the Bottom face
        row = 5
        # Column set to three to swap everything before the last three columns
        # with the values at the last three columns
        column = -3

        # Swaps the values stated above
        self[row, :] = np.concatenate((self[row, column:], self[row, :column]))

        # Rotates the Bottom face
        self[6:9, 3:6] = np.rot90(self[6:9, 3:6], k=3)

    if move == 'F':
        # Simply rotates the Front 5x5 grid clockwise
        self[2:7, 2:7] = np.rot90(self[2:7, 2:7], k=3)

    if move == 'B':
        # To simulate an F turn, a 5x5 grid is made using
        # The last four columns on the middle rows of hte 5x5 grid
        # The first column on the last column of the 5x5 grid
        # The first row on the first row of the 5x5 grid
        # The last row on the last row of the 5x5 grid
        temp = np.array([[' ' for _ in range(5)] for _ in range(5)])
        temp[1:4, :4] = np.array(self[3:6, 8:12])
        temp[0, 1:4] = np.array(np.flip(self[0, 3:6]))
        temp[1:4, 4] = np.array(self[3:6, 0])
        temp[4, 1:4] = np.array(np.flip(self[8, 3:6]))

        temp = np.rot90(temp, k=3)

        # Places the temp 5x5 grid back into self
        # Doing the above process in reverse
        self[3:6, 8:12] = temp[1:4, :4]
        self[8, 3:6] = np.flip(temp[4, 1:4])
        self[3:6, 0] = temp[1:4, 4]
        self[0, 3:6] = np.flip(temp[0, 1:4])

    if move == 'RPRIME':
        # temp array to store the list of the values being moved
        temp = []

        # Moving the Right face in any direction requires the values
        # at column 5 and the values at column 9
        column = 5
        otherColumn = 14 - column

        # Any value moving between column and otherColumn must be flipped

        # Assigns three values at Column 5 to temp
        temp[0:6] = [self[row][column] for row in range(6)]
        # Assigns the other six values at Column 5 to temp
        temp[6:9] = [self[row][column] for row in range(6, 9)]
        temp[6:9] = np.flip(temp[6:9])
        # Assigns the otherColumn's three values at Column 9 to temp and then flips it
        temp[9:12] = [self[row][otherColumn] for row in range(3, 6)]
        temp[9:12] = np.flip(temp[9:12])
        # Reorders the list to place them back into self
        temp = temp[-3:] + temp[:-3]

        # Places the temp values back into self
        for row in range(9):
            self[row][column] = temp[row]

        for row in range(3, 6):
            self[row][otherColumn] = temp[row + 6]

        # Moving the Right face also rotates the Right side
        # Since np.rot rotates counter clockwise, k must be three to simulate
        # a clockwise turn.
        self[3:6, 6:9] = np.rot90(self[3:6, 6:9])

    if move == 'LPRIME':
        # temp array to store the list of the values being moved
        temp = []

        # Moving the Left face in any direction requires the values
        # at column 5 and the values at column 9
        column = 3
        otherColumn = 14 - column

        # Any value moving between column and otherColumn must be flipped

        # Assigns three values at Column 5 to temp and then flips it
        temp[0:3] = [self[row][column] for row in range(3)]
        temp[0:3] = np.flip(temp[0:3])

        # Assigns the other six values at Column 5 to temp No need to flip
        temp[3:9] = [self[row][column] for row in range(3, 9)]

        # Assigns the otherColumn's three values at Column 9 to temp and then flips it
        temp[9:12] = [self[row][otherColumn] for row in range(3, 6)]
        temp[9:12] = np.flip(temp[9:12])

        # Reorders the list to place them back into self
        temp = temp[3:] + temp[:3]

        # Places the temp values back into self
        for row in range(9):
            self[row][column] = temp[row]

        for row in range(3, 6):
            self[row][otherColumn] = temp[row + 6]

        # Moving the Left face also rotates the Left side
        # Since np.rot rotates counter clockwise, k must be three to simulate
        # a clockwise turn.
        self[3:6, 0:3] = np.rot90(self[3:6, 0:3])

    if move == 'UPRIME':
        # Works in the third row to rotate the Top face
        row = 3
        # Column set to three to swap everything before the last three columns
        # with the values at the last three columns
        column = -3

        # Swaps the values stated above
        self[row, :] = np.concatenate((self[row, column:], self[row, :column]))

        # Rotates the Top face
        self[0:3, 3:6] = np.rot90(self[0:3, 3:6])

    if move == 'DPRIME':
        # Works in the third row to rotate the Bottom face
        row = 5
        # Column set to three to swap everything after the first three columns
        # with the values at the first three columns
        column = 3

        # Swaps the values stated above
        self[row, :] = np.concatenate((self[row, column:], self[row, :column]))

        # Rotates the Bottom face
        self[6:9, 3:6] = np.rot90(self[6:9, 3:6])

    if move == 'FPRIME':
        # Simply rotates the Front 5x5 grid counterclockwise
        self[2:7, 2:7] = np.rot90(self[2:7, 2:7])

    if move == 'BPRIME':
        # To simulate an F turn, a 5x5 grid is made using
        # The last four columns on the middle rows of hte 5x5 grid
        # The first column on the last column of the 5x5 grid
        # The first row on the first row of the 5x5 grid
        # The last row on the last row of the 5x5 grid
        temp = np.array([[' ' for _ in range(5)] for _ in range(5)])
        temp[1:4, :4] = np.array(self[3:6, 8:12])
        temp[0, 1:4] = np.array(np.flip(self[0, 3:6]))
        temp[1:4, 4] = np.array(self[3:6, 0])
        temp[4, 1:4] = np.array(np.flip(self[8, 3:6]))

        temp = np.rot90(temp)

        # Places the temp 5x5 grid back into self
        # Doing the above process in reverse
        self[3:6, 8:12] = temp[1:4, :4]
        self[8, 3:6] = np.flip(temp[4, 1:4])
        self[3:6, 0] = temp[1:4, 4]
        self[0, 3:6] = np.flip(temp[0, 1:4])