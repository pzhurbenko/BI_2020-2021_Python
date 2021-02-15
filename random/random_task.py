import numpy as np
import random
import timeit
import matplotlib.pyplot as plt


# Время работы numpy
size = [1]
time = [0]
while size[-1] < 1000000:
    rng = np.random.default_rng()
    
    start = timeit.default_timer()
    rng.uniform(0, 1, size = size[-1])
    stop = timeit.default_timer()
    
    size.append(size[-1] + 50000)
    time.append(round((stop - start), 5))
# print(size)
# print(time)

# Время работы random
size_rn = [1]
time_rn = [0]
while size_rn[-1] < 1000000:
    start = timeit.default_timer()
    array = []
    for i in range(1, size_rn[-1]):
        ran = random.random()
        array.append(ran)
    stop = timeit.default_timer()
    size_rn.append(size_rn[-1] + 50000)
    time_rn.append(round((stop - start), 5))
# print(size_rn)
# print(time_rn)

# визуализация
plt.plot(size, time, label = "numpy")
plt.plot(size_rn, time_rn, label = "random")

plt.xlabel('Generated numbers')
plt.ylabel('Time')


plt.title('Time comparing between numpy and random')

plt.legend()
plt.show()
# plt.savefig("numpy vs random")




