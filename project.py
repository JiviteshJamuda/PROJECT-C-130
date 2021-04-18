import pandas as pd
import csv

df = pd.read_csv('merged_data.csv')
df = df.drop([0], axis=0)
del df['luminosity']
df.dropna()
# print(df.shape)
df.to_csv('final.csv')