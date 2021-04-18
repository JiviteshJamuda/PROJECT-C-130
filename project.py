import pandas as pd
import csv

df = pd.read_csv('merged_data.csv')
print(df.head())
# print(df.shape)
del df['luminosity']
df.dropna()
# print(df.shape)
# print(list(df))

df.to_csv('final.csv')