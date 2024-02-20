def matrix(m,n):
    mat = []
    print("Enter the elements of the matrix")
    for i in range(m):
        row = []
        for j in range(n):
            value = int(input())
            row.append(value)
        mat.append(row)
    print(*mat,sep="\n")
    print("\n")
    return(mat)

def multiply(matrix_A,matrix_B,matrix_C):
    for i in range(0,len(matrix_C)):
        for j in range(0,len(matrix_C[0])):
            for k in range(0,len(matrix_B)):
                matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
                
    print(*matrix_C,sep="\n")
    return matrix_C
                

print("Enter the size of Matrix A")
m = int(input("Enter the row:"))
n = int(input("Enter the column:"))
matrix_A = matrix(m,n)
print("Enter the size of Matrix B")
m1 = int(input("Enter the row:"))
n1 = int(input("Enter the column:"))
matrix_B = matrix(m1,n1)
print("Enter the value of matrix C as 0 only:")
matrix_C = matrix(m,n1)
multiply(matrix_A,matrix_B,matrix_C)