# sudoku solver in python

sudokuEx01 = [[0, 0, 7, 0, 4, 0, 0, 0, 0],
              [3, 0, 5, 0, 0, 6, 0, 0, 7],
              [9, 2, 0, 7, 9, 0, 0, 1, 0],
              [0, 3, 0, 0, 2, 0, 0, 7, 4],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [5, 7, 0, 0, 6, 0, 0, 9, 0],
              [0, 1, 0, 0, 5, 9, 0, 6, 8],
              [6, 0, 0, 8, 0, 0, 1, 0, 3],
              [0, 0, 0, 0, 3, 0, 2, 0, 0]]


def createMatrix():  # creates a 9x9 matrix
    sudoku = list(range(9))
    for xi in range(9):
        sudoku[xi] = list(range(9))

    return sudoku


def printSudoku(sudoku):    # display the matrix
    for x in range(9):
        print(sudoku[x][0][0], sudoku[x][1][0], sudoku[x][2][0],
              sudoku[x][3][0], sudoku[x][4][0], sudoku[x][5][0],
              sudoku[x][6][0], sudoku[x][7][0], sudoku[x][8][0])


def startSudoku(sudoku):    # starts the matrix Z axis
    for x in range(9):
        for y in range(9):
            sudoku[x][y] = list(range(10))

    return sudoku


def sudokuEntry(sudoku, entry):
    for x in range(9):
        for y in range(9):
            sudoku[x][y][0] = entry[x][y]
    return sudoku   # enters the problem to solve in the Z0 level


def squareCheck(sudoku, possList, rx, rxm, ry, rym):  # checks number in the square...
    for xi in range(rx, rxm):
        for yi in range(ry, rym):
            if sudoku[xi][yi][0] in possList and sudoku[xi][yi] != 0:
                poss = possList.index(sudoku[xi][yi][0])
                possList.pop(poss)

    return possList


def checkXY(sudoku, x, y):  # reciveis a position with unknown, checks the possibilities and returns a smaller list
    possList = sudoku[x][y]

    for xi in range(1, 9):     # checking the matrix in the X direction
        if sudoku[xi][y][0] in possList and sudoku[xi][y][0] != 0:
            poss = possList.index(sudoku[xi][y][0])
            possList.pop(poss)

    for yi in range(1, 9):
        if sudoku[x][yi][0] in possList and sudoku[x][yi][0] != 0:
            poss = possList.index(sudoku[x][yi][0])
            possList.pop(poss)

    if x in range(0, 2):
        if y in range(0, 2):
            possList = squareCheck(sudoku, possList, 0, 2, 0, 2)
        if y in range(3, 5):
            possList = squareCheck(sudoku, possList, 0, 2, 3, 5)
        if y in range(6, 8):
            possList = squareCheck(sudoku, possList, 0, 2, 6, 8)
    if x in range(3, 5):
        if y in range(0, 2):
            possList = squareCheck(sudoku, possList, 3, 5, 0, 2)
        if y in range(3, 5):
            possList = squareCheck(sudoku, possList, 3, 5, 3, 5)
        if y in range(6, 8):
            possList = squareCheck(sudoku, possList, 3, 5, 6, 8)
    if x in range(7, 9):
        if y in range(0, 2):
            possList = squareCheck(sudoku, possList, 6, 8, 0, 2)
        if y in range(3, 5):
            possList = squareCheck(sudoku, possList, 6, 8, 3, 5)
        if y in range(6, 8):
            possList = squareCheck(sudoku, possList, 6, 8, 6, 8)

    return possList


def scanSudoku(sudoku):
    for xi in range(9):
        for yi in range(9):
            if len(sudoku[xi][yi]) > 2:
                sudoku[xi][yi] = checkXY(sudoku, xi, yi)
            else:
                sudoku[xi][yi][0] = sudoku[xi][yi][1]

    return sudoku  # scan the matrix XY for unsolved fields


def sudokuEnd(sudoku):
    for xi in range(9):
        for yi in range(9):
            if sudoku[xi][yi][0] == 0:
                return False
    return True  # checks to see if the problem is done...


# RUN

SUDO = createMatrix()
SUDO = startSudoku(SUDO)
printSudoku(SUDO)
sudokuEntry(SUDO, sudokuEx01)
printSudoku(SUDO)
for i in range(0, 9):
    check
