global N
# function to check if a queen can be placed on Game_board[row][column]. 
def SafeOrNot(Game_board, row, column ,N):
  
    # Check this row on left side
    for i in range(column):
        if Game_board[row][i] == 1:
            return False
  
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if Game_board[i][j] == 1:
            return False
  
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(column, -1, -1)):
        if Game_board[i][j] == 1:
            return False
  
    return True
  
def Solve_Until_Found(Game_board, column , N): #return true if found else false
    if column >= N:
        return True

    for i in range(N):
  
        if SafeOrNot(Game_board, i, column, N):
            Game_board[i][column] = 1
  
            if Solve_Until_Found(Game_board, column + 1,N) == True:
                return True
            Game_board[i][column] = 0
  
    # if the queen can not be placed in any row in
    # this columnum column  then return false
    return False

def Displaysol(Game_board,N):
    for i in range(N):
        for j in range(N):
            print(Game_board[i][j] , end = " "),
        print()

def SolveNQueenProblem():
    N = input("Enter the value of N ")
    N = int(N)
    Game_board=[]

    for i in range(N):
        row=[]
        for j in range(N):
            row.append(0)
        Game_board.append(row)
  
    if Solve_Until_Found(Game_board, 0 ,N) == False:
        print ("Solution does not exist")
        return False
  
    Displaysol(Game_board,N)
    return True

SolveNQueenProblem()