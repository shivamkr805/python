print("hello world")

sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]





def possibleOutcome(sudoku,row,col):
    # checking column-wise
    possibleMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 9):  # Check all 9 rows
        if sudoku[i][col]  in possibleMoves:
            possibleMoves.remove(sudoku[i][col])
    # Check all 9 rows
    for i in range(0, 9): 
        if sudoku[row][i]  in possibleMoves:
            possibleMoves.remove(sudoku[row][i])
 
    newRow = (row // 3) * 3 
    newCol = (col // 3) * 3 
    for i in range(3):
        for j in range(3):
           if sudoku[newRow+i][newCol+j]  in possibleMoves:
            possibleMoves.remove(sudoku[newRow+i][newCol+j]) 
    return possibleMoves
def FindemptyCells(sudoku):
    emptyCells=[]
    # printing the solution 
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                emptyCells.append([i,j])
    return emptyCells
        

def dfs(sudoku): 
    emptyCells=FindemptyCells(sudoku_puzzle)
    if len(emptyCells) ==0 :
        # print("return by empty cell")
        print("solution")
        for i in range(9):
            print(sudoku[i],",")
        return True
    initialPosition=emptyCells[0]
    # print("intialPostiin",initialPosition)
    possible_numbers = possibleOutcome(sudoku,initialPosition[0],initialPosition[1])
    if(len(emptyCells) !=0 and possible_numbers==0):
        # print("return by mistake")
        return sudoku
    for i in range(len(possible_numbers)):
        sudoku[initialPosition[0]][initialPosition[1]]=possible_numbers[i]
        result=dfs(sudoku)
        if result:  # If solution is found, stop further recursion
            return True
        sudoku[initialPosition[0]][initialPosition[1]]=0
    # print("return by ending")
    return False
result=dfs(sudoku_puzzle)

    # print("\n")
# print("Possible numbers remaining:", possible_numbers)
# print("empty cells",emptyCells)
