import plotly as plt
import numpy as np
import sys

print('Введите количество шагов: ')
l = int(input())

# random walk
x_position, y_position = [0], [0]
direction = np.random.choice([-1, 1], size = l)
for i in direction:
    if i == 1:
        x_position.append(x_position[-1] + np.random.choice([-1, 1]))
        y_position.append(y_position[-1])
    if i == -1:
        y_position.append(y_position[-1] + np.random.choice([-1, 1]))
        x_position.append(x_position[-1])

# визуализация
fig = plt.graph_objects.Figure(data=plt.graph_objects.Scatter(
    x = x_position,
    y = y_position,
    mode = 'markers',
    name = 'Random walk 2D',
    marker = dict(
        color = np.arange(l),
        size = 8,
        colorscale = 'Reds',
        showscale = True
    )
))

fig.show()






