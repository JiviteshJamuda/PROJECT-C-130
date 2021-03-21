import pandas as pd
import csv

df = pd.read_csv('merged_data.csv')
# print(df.shape)
del df['luminosity']
del df['Serial number']
# print(df.shape)
# print(list(df))

df.to_csv('final.csv')