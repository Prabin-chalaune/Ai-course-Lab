#Backtracking approach
import pprint

# n=int(input("Enter number of quees:"))
# board=[['']*n for i in range(n)]

def display(board):
    for row in board:
        print(row);

def isSafe(board,x,y,n):
    #column test
    for row in range(x):
        if board[row][y]=="Q":
            return False;

        #top left diagnal test
        r=x-1
        c=y-1
        while(r>=0 and c>=0):
            if board[r][c] == "Q":
                return False
            r-=1
            c-=1

        #top right diagnal test
        r=x-1
        c=y+1
        while(r>=0 and c<n):
            if board[r][c] == "Q":
                return False;
            r-=1;
            c+=1;

    return True;

def nQeensSolver(board,x,n):
    if(x>=n):
        return False

    for col in range(n):
        if(isSafe(board,x,col,n)):
            board[x][col] ="Q"

            if(nQeensSolver(board,x+1,n)):
                return True;
            board[x][col] = ' '
    return False


if __name__ =='__main__':
    n=int(input("Enter number of quees:"))
    board=[['']*n for i in range(n)]

    if(nQeensSolver(board,0,n)):
        display(board);
    else:
        print("Not found")




# board[0][0]=="Q"
# print(isSafe(board,2,0,n))
# display();
#Lab task:  sudoku solver using backtracking