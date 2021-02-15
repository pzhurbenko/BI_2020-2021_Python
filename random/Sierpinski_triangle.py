import numpy as np
from math import sqrt
import plotly as plt
from random import random, randint

# Треугольник
corner = [(0, 0), (5, 5), (10, 0)]

# Середина
def middle(a, b):
    return (0.5*(a[0] + b[0]), 0.5*(a[1] + b[1]))

l = 50000
x = np.zeros(l)
y = np.zeros(l)

x[0] = np.random.randint(0, 2)
y[0] = np.random.randint(0, 2)
for i in range(1, l):
    k = np.random.randint(0, 3)
    x[i], y[i] = middle(corner[k], (x[i-1], y[i-1]))
    
fig = plt.graph_objects.Figure(data=plt.graph_objects.Scatter(
    x = x,
    y = y,
    mode = 'markers',
    name = 'Sierpinski',
    marker = dict(
        color = np.arange(l),
        size = 4,
        colorscale = 'Reds',
        showscale = True
    )
))


fig.show()
