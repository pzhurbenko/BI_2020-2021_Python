import numpy as np
import random
import timeit
import matplotlib.pyplot as plt

# проверка отсортирован ли список
def if_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# сортировка monkey sort
def bogosort(lst):
    while not if_sorted(lst):
        random.shuffle(lst)
    return lst

# генерация списков    
global_time = []
for j in range(1, 101):
    time = []
    for i in range(1, 12, 1):
        lst = np.random.randint(0, 4, i)
        
        start = timeit.default_timer()
        bogosort(lst)
        # print(lst)
        stop = timeit.default_timer()
    
        time.append(round((stop - start), 6))
    
    global_time.append(time)
# print(global_time)

# расчет среднего и ст. откл.
time_std = []
time_mean = []
for j in range(0, 11):
    time_temp = []
    for i in global_time:
        time_temp.append(i[j])
    std = np.std(time_temp)
    mean = np.mean(time_temp)
    time_std.append(std)
    time_mean.append(mean)

# print(time_std)
# print(time_mean)

# визуализация
x = np.array(list(range(1, 12)))
y = np.array(time_mean)
e = np.array(time_std) 

plt.errorbar(x, y, e, linestyle='None', marker='^')
plt.xlabel('Length of the list')
plt.ylabel('Time, min')


plt.title('List sorting time with bogosort algorithm. Mean and std are shown')

plt.show()
	

