# sudoku solver in python


sudokuEx01 = [[0, 0, 7, 0, 4, 0, 0, 0, 0],  # sudoku aberto...
              [3, 0, 5, 0, 0, 6, 0, 0, 7],
              [9, 2, 0, 7, 9, 0, 0, 1, 0],
              [0, 3, 0, 0, 2, 0, 0, 7, 4],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [5, 7, 0, 0, 6, 0, 0, 9, 0],
              [0, 1, 0, 0, 5, 9, 0, 6, 8],
              [6, 0, 0, 8, 0, 0, 1, 0, 3],
              [0, 0, 0, 0, 3, 0, 2, 0, 0]]

sudokuEx02 = [[0, 2, 0, 4, 5, 6, 7, 8, 9],
              [4, 5, 7, 0, 8, 0, 2, 3, 6],
              [6, 8, 9, 2, 3, 7, 0, 4, 0],
              [0, 0, 5, 3, 6, 2, 9, 7, 4],
              [2, 7, 4, 0, 9, 0, 6, 5, 3],
              [3, 9, 6, 5, 7, 4, 8, 0, 0],
              [0, 4, 0, 6, 1, 8, 3, 9, 7],
              [7, 6, 1, 0, 4, 0, 5, 2, 8],
              [9, 3, 8, 7, 2, 5, 0, 6, 0]]

sudokuEx03 = [[0, 2, 0, 4, 0, 6, 0, 0, 9],
              [4, 0, 7, 0, 8, 0, 2, 3, 6],
              [0, 8, 0, 2, 0, 7, 0, 4, 0],
              [0, 0, 0, 0, 0, 2, 0, 7, 0],
              [0, 0, 4, 0, 0, 0, 6, 5, 0],
              [3, 9, 0, 5, 0, 0, 0, 0, 0],
              [0, 0, 0, 6, 0, 8, 0, 9, 7],
              [7, 6, 1, 0, 4, 0, 5, 2, 8],
              [0, 3, 0, 7, 2, 5, 0, 6, 0]]

sudokuEx04 = [[9, 0, 7, 0, 1, 0, 0, 4, 0],  # open...
              [0, 8, 2, 0, 0, 4, 0, 0, 7],
              [1, 4, 0, 7, 3, 0, 0, 0, 0],
              [0, 0, 0, 4, 0, 7, 0, 0, 3],
              [0, 7, 0, 0, 0, 0, 0, 2, 0],
              [2, 0, 0, 5, 0, 9, 0, 0, 0],
              [0, 0, 0, 0, 4, 3, 0, 9, 8],
              [7, 0, 0, 6, 0, 0, 1, 3, 0],
              [0, 9, 0, 0, 7, 0, 6, 0, 2]]

sudokuEx05 = [[6, 0, 0, 7, 0, 0, 0, 0, 0],
              [0, 8, 0, 0, 6, 4, 0, 0, 5],
              [0, 0, 5, 0, 1, 8, 0, 0, 0],
              [2, 0, 4, 0, 7, 3, 5, 0, 8],
              [0, 6, 0, 8, 4, 9, 0, 3, 0],
              [7, 0, 8, 5, 2, 0, 4, 0, 1],
              [0, 0, 0, 4, 8, 0, 3, 0, 0],
              [1, 0, 0, 3, 5, 0, 0, 7, 0],
              [0, 0, 0, 0, 0, 7, 0, 0, 2]]

sudokuEx06 = [[0, 0, 7, 0, 4, 0, 0, 0, 0],  # sudoku aberto...
              [3, 0, 5, 0, 0, 6, 0, 0, 7],
              [9, 2, 0, 7, 9, 0, 0, 1, 0],
              [0, 3, 0, 0, 2, 0, 0, 7, 4],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [5, 7, 0, 0, 6, 0, 0, 9, 0],
              [0, 1, 0, 0, 5, 9, 0, 6, 8],
              [6, 0, 0, 8, 0, 0, 1, 0, 3],
              [0, 0, 0, 0, 3, 0, 2, 0, 0]]


def create999Matrix(problem):   # creates a 9x9x9 matrix with the possible numbers in the Z axis; returns list
    matrix = list(range(9))
    for xi in range(9):
        matrix[xi] = list(range(9))
    for xi in range(9):
        for yi in range(9):
            if problem[xi][yi] == 0:
                matrix[xi][yi] = list(range(1, 10))
            else:
                matrix[xi][yi] = list([problem[xi][yi]])
    return matrix


def printMatrix(matrix):    # takes a 9x9 matrix and prints it
    for xi in range(9):
        print(matrix[xi][0], matrix[xi][1], matrix[xi][2],
              matrix[xi][3], matrix[xi][4], matrix[xi][5],
              matrix[xi][6], matrix[xi][7], matrix[xi][8])


def scanXY(matrix, solMatrix, X, Y):    # takes a sudoku problem, a possible solutions matrix and coordenates and scans in the X and Y axis; returns an updated solution matrix
    print('>>> scanXY starting...')
    for xi in range(9):  # checking X axis
        #print('>> scanning coordenates:', xi, Y)
        if matrix[xi][Y] in solMatrix[X][Y] and X != xi and matrix[X][Y] == 0:
            print('>> found match:', matrix[xi][Y], 'in coordenates:', xi, Y)
            matchX = solMatrix[X][Y].index(matrix[xi][Y])
            solMatrix[X][Y].pop(matchX)
            print('> new solMatrix=', solMatrix[X][Y])
    for yi in range(9):  # checking Y axis
        #print('>> scanning coordenates:', X, yi)
        if matrix[X][yi] in solMatrix[X][Y] and Y != yi and matrix[X][Y] == 0:
            print('>> found match:', matrix[X][yi], 'in coordenates:', X, yi)
            matchY = solMatrix[X][Y].index(matrix[X][yi])
            solMatrix[X][Y].pop(matchY)
            print('> new solMatrix=', solMatrix[X][Y])
    # print('=======================================')
    return solMatrix


def SQcheck(matrix, X, Y, solMatrix, rx, rxm, ry, rym):
    #print('>>> scanning range:', rx, rxm, 'X', ry, rym, 'coordenates:', X, Y)
    for xi in range(rx, rxm + 1):
        for yi in range(ry, rym + 1):
            #print('>>> scanning coordenates:', xi, yi,)
            if matrix[xi][yi] in solMatrix[X][Y] and (X != xi and Y != yi) and matrix[X][Y] == 0:
                print('>> found match:', matrix[xi][yi], 'in coordenates:', xi, yi)
                matchSQ = solMatrix[X][Y].index(matrix[xi][yi])
                solMatrix[X][Y].pop(matchSQ)
                print('> new solMatrix=', solMatrix[X][Y])
    return solMatrix


def scanSQ(matrix, solMatrix, X, Y):    # takes a sudoku problem, a possible solutons matrix and coordenates and scans the square locus; returns an updated solution matrix
    print('>>> scanSQ starting...')
    if X in range(0, 3):
        if Y in range(0, 3):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 0, 2, 0, 2)
        if Y in range(3, 6):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 0, 2, 3, 5)
        if Y in range(6, 9):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 0, 2, 6, 8)
    if X in range(3, 6):
        if Y in range(0, 3):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 3, 5, 0, 2)
        if Y in range(3, 6):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 3, 5, 3, 5)
        if Y in range(6, 9):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 3, 5, 6, 8)
    if X in range(6, 9):
        if Y in range(0, 3):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 6, 8, 0, 2)
        if Y in range(3, 6):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 6, 8, 3, 5)
        if Y in range(6, 9):
            solMatrix = SQcheck(matrix, X, Y, solMatrix, 6, 8, 6, 8)
    # print('=======================================')
    return solMatrix


def scansolMatrix(matrix, solMatrix):   # scan solMatrix for solved fields; returns solved matrix
    for xi in range(9):
        for yi in range(9):
            if len(solMatrix[xi][yi]) == 1:
                matrix[xi][yi] = solMatrix[xi][yi][0]
    return matrix


def scanEND(matrix):  # scans the sudoku matrix for zeros; returns True for a complete sudoku
    for xi in range(9):
        if 0 in matrix[xi]:
            return False
    return True


sudoku = sudokuEx02
sol = create999Matrix(sudoku)
print('=======================================')
print('==========SUDOKU SOLVER START==========')
print('=======================================')
printMatrix(sudoku)
print('=======================================')
print('=======================================')
flag = 1
inter = 0
stopFlag = 0
while flag == 1:
    for xi in range(9):
        for yi in range(9):
            print('=======> scannig coord:', xi, yi, 'field value:', sudoku[xi][yi])
            if sudoku[xi][yi] == 0:
                sol = scanSQ(sudoku, sol, xi, yi)
                sol = scanXY(sudoku, sol, xi, yi)
            else:
                print('>>> field skipped...')

    scansolMatrix(sudoku, sol)
    print('=================INTERATION END======================')
    printMatrix(sudoku)
    print('===================solMatrix=========================')
    printMatrix(sol)
    print('=====================================================')
    inter = inter + 1
    print('Interation:', inter)
    solold = sol
    if scanEND(sudoku) == True:
        print('its DONE!')
        flag = 0
    else:
        if solold == sol:
            stopFlag = stopFlag + 1
            if stopFlag >= 100:
                print('This sudoku is open')
                flag = 0
            else:
                flag = 1  # int(input('enter 1 to continue...'))
