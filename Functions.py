#List of functions
# 1.Gauss Jordan
# 2.Partial Pivot
# 3.Matrix multiplication
# 4.Forward substitution
# 5.Reverse substitution
# 6.LU decomposition

def GaussJordan(A, B):
    # the pivot row
    pivot = A[k][k]
    for i in range(k, n):
        A[k][i] /= pivot
    B[k] = B[k] / pivot
    # other rows
    for i in range(n):
        if A[i][k] == 0 or i == k:
            continue
        else:
            term = A[i][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - term * A[k][j]
            B[i] = B[i] - term * B[k]
    return B

def Parpivot(A,B,k):
    if A[k][k] == 0:
        for i in range(k + 1, 4):
            if abs(A[i][k]) > abs(A[k][k]) and abs(A[k][k]) == 0:
                A[k], A[i] = A[i], A[k]
                B[k], B[i] = B[i], B[k]
    return A, B

def MatrixMultiply(M,A):
    B=[]
    for i in range(len(M)):
        row =[]
        for j in range(len(A[0])):
            row.append(0)
        B.append(row)

    for x in range(len(M)):
        for y in range(len(A[0])):
            for z in range(len(M[0])):
                B[x][y] += M[x][z] * A[z][y]
    return B


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

    print("The combined L-U matrix",A)
    return A
