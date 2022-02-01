import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Иван', 'Анна', 'Мария', 'Василий', 'Анастасия'],
    'math': [5, 3, 3, 4, 4],
    'russian': [4, 4, 4, 5, 3],
    'history': [5, 4, 3, 4, 5]})

df['mean'] = (df['math'] + df['russian'] + df['history']) / 3
print(df)
print()
df['класс'] = ['11A', '11А', '11Б', '11Г', '11Б']
print(df)
print()
df.drop(labels=df[df['name'] == 'Анастасия'].index, inplace=True)
print(df)
print()
series = [df.loc[0][:4], df.loc[3][:4]]
print(pd.concat(series, axis=1))
