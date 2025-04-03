import math
import numpy as np

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

def calcJacobian(x1, x2):
    jacob = [[0, 0],[0, 0]]
    jacob[0][0] = 1 + (3 / x1)
    jacob[0][1] = -2 * x2
    jacob[1][0] = 4 * x1 - x2 - 5
    jacob[1][1] = -x1
    return jacob

def newtonsMethod(estimates, tol=1e-6, max_iter=50, damping_factor = 0.5):
    x1 = estimates[0]
    x2 = estimates[1]
    jacob = calcJacobian(x1, x2)
    f1 = x1 + (3 * math.log(abs(x1))) - (x2 ** 2)
    f2 = 2 * (x1 ** 2) - x1 * x2 - 5 * x1 + 1
    jacob[0].append(-f1)
    jacob[1].append(-f2)
    sol = Gauss(jacob)
    estimates[0] = estimates[0] + damping_factor * sol[0]
    estimates[1] = estimates[1] + damping_factor * sol[1]

    norm = math.sqrt(sol[0]**2 + sol[1]**2)
    if norm < tol:
        return estimates, True
    return estimates, False

counter = 0
estimates = [2, 1]
tolerance = 10 ** -7
max_iterations = 50

while counter < max_iterations:
    estimates, converged = newtonsMethod(estimates, tol=tolerance)
    print(estimates)
    if converged:
        print(f"Converged to solution: {estimates} in {counter + 1} iterations.")
        break
    counter += 1

if not converged:
    print("Did not converge within the maximum number of iterations.")
