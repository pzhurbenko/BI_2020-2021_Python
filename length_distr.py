import collections
import matplotlib
import matplotlib.pyplot as plt

input_file = input('введите название файла: ')

with open(input_file, 'r') as fa_in:
    lines = []
    dic = {}
    count = 0
    start = 1
    for line in fa_in:
        line.rstrip()
        count += 1
        if count % 2 == 0:
            ll = len(line)
            if dic.get(ll) != None:
                dic[ll] = int(dic[ll]) + 1
            else:
                dic[ll] = 1
        else:
    	    pass

sorted_dic = collections.OrderedDict(sorted(dic.items()))

length = list(sorted_dic.keys())         
values = list(sorted_dic.values())  

fig, ax = plt.subplots()
ax.plot(length, values)

ax.set(xlabel='Длина, п.н.', ylabel='Кол-во последовательностей',
       title='Распределение длин последовательностей')
ax.grid()

fig.savefig("test.png")
plt.show()


