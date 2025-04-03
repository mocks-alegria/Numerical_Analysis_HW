x = [0.5, 0.59588511, 0.61224831, 0.61494177, 0.61538219, 0.61545413, 0.61546588, 0.6154678, 0.61546811, 0.61546816]
x_carrot = []
ratios = []

# Calculate ratios from original x values
for i in range(1, len(x) - 1):
    ratio = (x[i + 1] - x[i]) / (x[i] - x[i - 1])
    ratios.append(ratio)

# Calculate accelerated sequence using Aitken's Algorithm
for i in range(1, len(x) - 1):
    accelerated_value = x[i] - ((x[i + 1] - x[i]) ** 2) / ((x[i + 1] - x[i]) - (x[i] - x[i - 1]))
    x_carrot.append(accelerated_value)

for i in range(len(x_carrot)):
    print("x_carrot[{}]: {:.10f}, ratio: {:.10f}".format(i, x_carrot[i], ratios[i]))
