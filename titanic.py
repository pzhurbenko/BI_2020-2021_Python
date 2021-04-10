import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

path = "/home/pzhurb/bioinf/learn/python/pandas/titanic.csv"

df = pd.read_csv(path)
# how many columns / rows
print(df.shape)
# какие колонки
print(df.dtypes)
# сколько NA
print(df.isnull().sum())
# узнаем сколько выжило
survived_count = df.groupby('Survived')['Survived'].count()
print(survived_count)
# сколько выжило в зависимости от гендера
survived_sex = df.groupby('Sex')['Survived'].sum()
print(survived_sex)
# распределение по классам
pclass_count = df.groupby('Pclass')['Pclass'].count()
print(pclass_count)
# распределение по возрасту, построение гистограммы
ages = df[df['Age'].notnull()]['Age'].values
# создание аррея
ages_hist = np.histogram(ages, bins=[0,10,20,30,40,50,60,70,80,90])
ages_hist_labels = ['0–10', '11–20', '21–30', '31–40', '41–50', '51–60', '61–70', '71–80', '81–90']
plt.figure(figsize=(7,7))
plt.title('Age distribution')
plt.bar(ages_hist_labels, ages_hist[0])
plt.xlabel('Age')
plt.ylabel('No of passenger')
for i, bin in zip(ages_hist[0], range(9)):
    plt.text(bin, i+3, str(int(i)), fontsize=12,
    horizontalalignment='center', verticalalignment='center')
plt.show()

# распределение по каютам

def take_initial(x):
    return x[0]
# убираем NA
cabins = df['Cabin'].dropna()

# берем только первые буквы
cabins = cabins.apply(take_initial)

# подсчитываем количество типов кают
cabins_count = cabins.value_counts()
print(cabins_count, end='\n\n')

# график
plt.title('Cabin distribution')
plt.bar(cabins_count.index, cabins_count.values)
plt.show()






