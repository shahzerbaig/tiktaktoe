r  = 2
c = 2
matrix = []
for i in range(r):
    a = []
    for j in range(c):
        a.append("-")
    matrix.append(a)

def print_matrix():
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end='')
        print()

def input_():
    row = int(input("Enter the Row number"))
    col = int(input("Enter the col number"))
    matrix[row][col] = input("Enter 'X' or 'O' ")
    print_matrix()
print_matrix()
ch = 4
for k in range(ch):
    print(k)
    input_()

"""print(matrix)
print("change a number")
scol = int(input("Enter colum number"))
srow = int(input("Enter row number"))
matrix[scol][srow] = int(input("enter the number"))"""
