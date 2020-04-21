r  = 3
c = 3
matrix = [] #Board
for i in range(r):
    a = []
    for j in range(c):
        a.append("-")
    matrix.append(a)

def print_matrix(): #This is for printing the Current matrix(Board Game)
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end='')
        print()

def input_(word): #Takin the input
    row = int(input("Enter the Row number"))
    col = int(input("Enter the col number"))
    if word == "x" or word == "X":
        matrix[row][col] = input("Enter 'X' ")
        print_matrix()
    else:
        matrix[row][col] = input("Enter 'O' ")
        print_matrix()

print_matrix()

def check():
    if matrix[0][0] == "x" and matrix[1][0] == "x" and matrix[2][0] == "x" or matrix[0][1] == "x" and matrix[1][1] == "x" and matrix[2][1] == "x" or matrix[0][2] == "x" and matrix[1][2] == "x" and matrix[2][2] == "x" or matrix[2][0] == "x" and matrix[1][1] == "x" and matrix[0][2] == "x" or matrix[0][0] == "x" and matrix[0][1] == "x" and matrix[0][2] == "x" or matrix[1][0] == "x" and matrix[1][1] == "x" and matrix[1][2] == "x" or matrix[2][0] == "x" and matrix[2][1] == "x" and matrix[2][2] == "x":
        print("Player 1 win")
    elif matrix[0][0] == "o" and matrix[1][0] == "o" and matrix[2][0] == "o" or matrix[0][1] == "o" and matrix[1][1] == "o" and matrix[2][1] == "o" or matrix[0][2] == "o" and matrix[1][2] == "o" and matrix[2][2] == "o" or matrix[2][0] == "o" and matrix[1][1] == "o" and matrix[0][2] == "o" or matrix[0][0] == "o" and matrix[0][1] == "o" and matrix[0][2] == "o" or matrix[1][0] == "o" and matrix[1][1] == "o" and matrix[1][2] == "o" or matrix[2][0] == "o" and matrix[2][1] == "o" and matrix[2][2] == "o":
        print("Player 2 is a winner")
    else:
        print("Its a Tie")



ch = 9
chance_1=[1,3,5,7,9]
chance_2=[2,4,6,8]
count = 1
for k in range(ch):
    print(k)
    for i in range(9): #there is a problem in loopin(infinite loops)
        if count in chance_1:
            print('chance is at one! ')
            input_("x")
            count +=1
        elif:
            print('chance is at two!')
            input_("o")
            count += 1

check()
"""print(matrix)
print("change a number")
scol = int(input("Enter colum number"))
srow = int(input("Enter row number"))
matrix[scol][srow] = int(input("enter the number"))"""
