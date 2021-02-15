import numpy as np
import random
import timeit
import matplotlib.pyplot as plt

global_time = [[1, 2, 3], [2, 3, 4]]

time_std = []
time_mean = []
for j in range(0, 3):
    time_temp = []
    for i in global_time:
        time_temp.append(i[j])
    std = np.std(time_temp)
    mean = np.mean(time_temp)
    time_std.append(std)
    time_mean.append(mean)

# print(time_std)
# print(time_mean)


x = np.array(list(range(1, 4)))
y = np.array(time_mean)
e = np.array(time_std) 

plt.errorbar(x, y, e, linestyle='None', marker='*')

plt.show()
	
