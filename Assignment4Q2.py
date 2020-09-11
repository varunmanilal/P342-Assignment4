from Functions import *

#The forward substition for all columns of C
def Forwardeq(A,C):
    global M
    M =[]
    for i in range(4):
        M.append(fwrdsub(A,C[i]))


#The backward substition for all columns of C
def Backwardeq(A,M):
    global N
    N=[]
    for i in range(4):
        N.append(bkwdsub(A, M[i]))

def main():
    # reading the matrix A from a external file
    f1 = open("Q2matrix.txt", "r")
    a = f1.read()
    a1 = [item.split(' ') for item in a.split('\n')]
    A = [[0, 0, 0, 0], [0 ,0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for k in range(4):
            A[i][k] = float(a1[i][k])
    print("A matrix is:", A)
    #Identity matrix
    C = [[1, 0, 0, 0], [0 ,1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    #LU decomposition
    LUdecomp(A,C)
    #Finding determinant of LU matrix.A non-zero determinant implies inverse exists.
    determinant =1
    for k in range(4):
        determinant *= A[k][k]
    print("The determinant is :",determinant)

    Forwardeq(A,C)
    Backwardeq(A,M)
    #The transverse gives the inverse matrix
    Iv = [[N[j][i] for j in range(4)] for i in range(4)]

    #Rounding off the values
    for i in range(4):
        for j in range(4):
            Iv[i][j]= round(Iv[i][j],3)
    print("The inverse matrix is ",Iv)

main()

# A matrix is: [[0.0, 2.0, 8.0, 6.0], [0.0, 0.0, 1.0, 2.0], [0.0, 1.0, 0.0, 1.0], [3.0, 7.0, 1.0, 0.0]]
# The combined L-U matrix [[3.0, 7.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 2.0], [0.0, 2.0, 8.0, -12.0]]
# The determinant is : -36.0
# The inverse matrix is  [[-0.25, 1.667, -1.833, 0.333], [0.083, -0.667, 0.833, 0.0], [0.167, -0.333, -0.333, 0.0], [-0.083, 0.667, 0.167, 0.0]]
