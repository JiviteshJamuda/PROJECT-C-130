import pandas as pd
import csv

df = pd.read_csv('merged_data.csv')
print(df.shape)
df.drop(df.index[(df["mass"] == "?")],axis=0,inplace=True)
df.drop(df.index[(df["radius"] == "?")],axis=0,inplace=True)
print(df.shape)
del df['luminosity']
print(df.shape)
df.to_csv('final.csv')