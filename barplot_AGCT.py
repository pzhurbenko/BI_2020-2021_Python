import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "/home/pzhurb/bioinf/learn/python/pandas/train.csv"

df = pd.read_csv(path)

A = df['A']
G = df['G']
C = df['C']
T = df['T']

labels = df['pos']
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, A, width, label='A')
ax.bar(labels, G, width, label='G')
ax.bar(labels, C, width, label='C')
ax.bar(labels, T, width, label='T')

ax.set_ylabel('Scores')
ax.set_title('Scores by nucleotide rate')
ax.legend()

plt.show()
