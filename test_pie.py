import matplotlib.pyplot as plt
import numpy as np
		
fig, ax = plt.subplots()

size = 0.5

# данные
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

# labels
labels_in = 'Frogs', 'Hogs', 'Dogs', 'Logs', 'Cats', 'Bats'
labels_out = 'Survived', 'Died', 'Unknown'

# выбор цветовой схемы ввиде array
cmap = plt.get_cmap("tab20c") 

# выбор цветов из цветовой схемы
outer_colors = cmap(np.arange(3)*4) 
inner_colors = cmap([1, 2, 5, 6, 9, 10]) 

# outer circle
ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors, labels = labels_out,
       wedgeprops=dict(width=size, edgecolor='w'))

# inner circle
ax.pie(vals.flatten(), radius=1-size, autopct='%1.1f%%', colors=inner_colors, labels = labels_in, 
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Тестовый пирог')
plt.show()
