import math
approximation = 0
accuracy = math.pow(10, -5)
switch = False
counter = 0
start = 0
end = 0.5
m = 0

def y(input):
    return 4 * math.sin(input) - math.exp(input)

def y_prime(input):
    return 4 * math.cos(input) - math.exp(input)

# Bisection Method
while switch == False:
    m = (start + end) / 2
    if y(start) * y(m) <= 0:
        end = m
    else:
        start = m
    if abs(y((start + end) / 2)) <= accuracy:
        approximation = (start + end) / 2
        switch = True
    counter += 1

print("Bisection method approximation completed at the {}th iteration: zero is at x = {:.10f}".format(counter, approximation))

approximation = 0
switch = False
counter = 0
start = 0
end = 0.5

# Weighted Bisection Method
w = start
w_forward = 0
F = y(start)
G = y(end)
while switch == False:
    w_forward = (G * start - F * end) / (G - F)
    if y(start) * y(w_forward) <= 0:
        end = w_forward
        G = y(w_forward)
        if y(w) * y(w_forward) > 0:
            F = F / 2
        w = w_forward
    else:
        start = w_forward
        F = y(w_forward)
        if y(w) * y(w_forward) > 0:
            G = G / 2
        w = w_forward
    if abs(y((start + end) / 2)) <= accuracy:
        approximation = (start + end) / 2
        switch = True
    counter += 1

print("Weighted bisection method approximation completed at the {}th iteration: zero is at x = {:.10f}".format(counter, approximation))

approximation = 0
switch = False
counter = 0
start = 0
end = 0.5

# Secant Method
ladder = [0, 0.5, 0]
while switch == False:
    ladder[2] = (y(ladder[1]) * ladder[0] - y(ladder[0]) * ladder[1]) / (y(ladder[1]) - y(ladder[0]))
    if abs(y(ladder[2])) <= accuracy:
        approximation = ladder[2]
        switch = True
    else:
        ladder[0] = ladder[1]
        ladder[1] = ladder[2]
    counter += 1

print("Secant method approximation completed at the {}th iteration: zero is at x = {:.10f}".format(counter, approximation))

approximation = 0
switch = False
counter = 0
start = 0
end = 0.5

# Newton's Method
while switch == False:
    start = start - y(start) / y_prime(start)
    if abs(y(start)) <= accuracy:
        approximation = start
        switch = True
    counter += 1

print("Newton's method approximation completed at the {}th iteration: zero is at x = {:.10f}".format(counter, approximation))
