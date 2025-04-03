import math
import numpy as np

def iter(sol):
    lastSol = sol[-1]
    x1 = (1 / math.sqrt(5)) * lastSol[1]
    x2 = 0.25 * (math.sin(lastSol[0]) + math.cos(lastSol[1]))
    sol.append([x1, x2])

def elem_sub(sol):
    differences = []
    for i in range(2):
        differences.append(abs(sol[-1][i] - sol[-2][i]))
    ans = max(differences)
    return ans

sol = [[1/4, 1/4]]
iter(sol)
ans = elem_sub(sol)
print(ans)

while ans >= (10 ** (-5)):
    iter(sol)
    ans = elem_sub(sol)
    print(ans)

print(sol[-1])
