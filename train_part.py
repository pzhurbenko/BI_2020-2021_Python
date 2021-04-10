import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "/home/pzhurb/bioinf/learn/python/pandas/train.csv"

df = pd.read_csv(path)

matches_mean = df['matches'].mean()
df_mean_matches = df.query('matches > @matches_mean')
part_df = df_mean_matches[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]

print(part_df)
part_df.to_csv(r'/home/pzhurb/bioinf/learn/python/pandas/train_part.csv', index = False)
