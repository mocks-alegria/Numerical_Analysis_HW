import numpy as np
# Implementation of the Gaussian Elimination Algorithm without Partial Pivoting
def Gauss(Matrix):
    sol = [None] * len(Matrix)
    for i in range(len(Matrix)):
        if Matrix[i][i] == 0:
            p = i
            while Matrix[p][i] == 0:
                p += 1
            Matrix[i], Matrix[p] = Matrix[p], Matrix[i]
        for j in range(i + 1, len(Matrix)):
            m = Matrix[j][i] / Matrix[i][i]
            multi = np.array(Matrix[i])
            subtract = m * multi
            swap = np.array(Matrix[j]) - subtract
            Matrix[j] = swap.tolist()
    for i in range(len(Matrix) - 1, -1, -1):
        sum = 0
        for j in range(i + 1, len(Matrix)):
            sum += Matrix[i][j] * sol[j]
        sol[i] = (Matrix[i][len(Matrix)] - sum) / Matrix[i][i]

    return sol

matrix = [[2, 1, -1, 1, 3, 7], 
          [1, 0, 2, -1, 1, 2], 
          [0, -2, -1, 1, -1, -5], 
          [3, 1, -4, 0, 5, 6], 
          [1, -1, -1, -1, 1, 3]]
print(f"Solution to Concatenated Matrix: {Gauss(matrix)}")
