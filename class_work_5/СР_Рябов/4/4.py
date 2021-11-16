import pandas as pd

df = pd.read_csv("income_evaluation.csv", sep=',')
# print(df.columns)
print(len(df[' income']))
df = df.drop(df[df[' income'] == ' >50K'].index)
print(len(df[' income']))


