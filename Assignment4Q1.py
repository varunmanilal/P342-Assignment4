#for importing partial pivot
from Functions import *
#LU decomposition
def LUdecomp(A,C):
    for j in range(len(A)):
        Parpivot(A, C, j)
        for i in range(len(A)):
            if i<=j:
                sumt = 0
                for k in range(0, i):
                        sumt += A[i][k] * A[k][j]
                A[i][j] = A[i][j] - sumt
            if i>j:
                sumt =0
                for k in range(0, j):
                        sumt += A[i][k] * A[k][j]
                A[i][j] =(1/A[j][j])*(A[i][j]-sumt)

    print("The combined L-U matrix: ",A)
    return A
#forward substitution
def fwrdsub(A , B):
    global Y
    Y = []
    for k in range(len(A)):
        Y.append(float(0))
    for i in range(0,len(A)):
        val = 0
        for j in range(0,i):
            val+=A[i][j]*Y[j]
        Y[i] += B[i] - val
    return Y
#backward substitution
def bkwdsub(A , B):
    global X
    X = []
    for k in range(len(A)):
        X.append(float(0))
    for i in reversed(range(len(A))):
        val = 0
        for j in reversed(range(0,len(A))):
            if j>i:
                val += A[i][j]*X[j]
        X[i] += (1/A[i][i])*(B[i] - val)
    return X
def main():
    # reading the equations from a external file
    r = open("Amatrix.txt", "r")
    A = readfile(r)
    print("A matrix is:", A)
    # The RHS value of the equations is imported from external file and read
    p = open("Cmatrix.txt", "r")
    C = read1d(p)
    #LU decomposition
    A = LUdecomp(A,C)
    #forward substitution
    print("The Y matrix is ",fwrdsub(A,C))
    Y = fwrdsub(A,C)
    #Backward substitution
    print("The X matrix is ",bkwdsub(A,Y))

main()

#A matrix is: [[1.0, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, -1.0, 0.0], [2.0, 1.0, 3.0, -2.0]]
#The combined L-U matrix:  [[1.0, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, 2.0, -2.0], [2.0, 1.0, 1.5, -3.0]]
#The Y matrix is  [6.0, -3.0, -2.0, -6.0]
#The X matrix is  [1.0, -1.0, 1.0, 2.0]
