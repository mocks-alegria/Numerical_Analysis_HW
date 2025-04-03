import numpy as np
# Implementation of LU Factorization Algorithm
def LUFactor(A):
    L = [None] * len(A)
    for i in range(len(L)):
        L[i] = [0] * len(A)
    U = [None] * len(A)
    for i in range(len(U)):
        U[i] = [0] * len(A)
    for i in range(len(L)):
        L[i][i] = 1
    for i in range(len(A)):
        for j in range(i, len(A)):
            sum = 0
            for k in range(i):
                sum += L[i][k] * U[k][j]
            U[i][j] = (A[i][j] - sum) / L[i][i]
        for j in range(i+1, len(A)):
            sum = 0
            for k in range(i):
                sum += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - sum) / U[i][i]
    print("The LU Factorization is:")
    print(np.array(L))
    print(np.array(U))

A = [[2, 1, 0, 0],
     [-1, 3, 3, 0],
     [2, -2, 1, 4],
     [-2, 2, 2, 5]]

print("A:")
LUFactor(A)

B = [[2.121, -3.46, 0, 5.217],
     [0, 5.193, -2.197, 4.206],
     [5.132, 1.414, 3.141, 0],
     [-3.111, -1.732, 2.718, 5.212]]
print("B:")
LUFactor(B)
