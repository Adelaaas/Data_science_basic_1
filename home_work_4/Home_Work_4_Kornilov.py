import numpy as np
import pandas as pd

print("Задание 1")
r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
s = s.sort_values()
print(f'{s[s > 5][:1]}\n')

print("Задание 2")
df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41, 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])
print(f'кто старше 40:\n{df[df["возраст"] > 40]}\n')
print(f'кто имеет доход выше среднего по датасету:\n{df[df["доход"] > df["доход"].sum()/4]}\n')
print(f'кто имеет доход выше среднего по датасету, но надежность ниже среднего по датасету:\n{df.loc[(df["доход"] > df["доход"].sum()/4) & (df["надежность клиента (0..1)"] < df["надежность клиента (0..1)"].sum()/4)]}\n')
df['важность клиента'] = [100000 * 0.65, 80000 * 0.74, 150000 * 0.87, 60000 * 0.68]
df['возможная долгосрочность клиента'] = [100000 * 0.65 * (45 - df['возраст'].sum()/4), 80000 * 0.74 * (26 - df['возраст'].sum()/4), 150000 * 0.87 * (41 - df['возраст'].sum()/4), 60000 * 0.68 * (21 - df['возраст'].sum()/4)]
print(f'{df}\n')

print("Задание 3")
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})
df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})
df1 = pd.concat([df1, df2], axis=0, join="outer", ignore_index=True, verify_integrity=True)
df1 = df1.drop(columns=['ves', 'frukt'], inplace=False)
print(f'{df1.head(9)}\n')

print("Задание 4")
df = pd.DataFrame({
    'fruit': ['Apple', 'Watermelon', 'Cherry', 'Orange', 'Banana'],
    'price': [25, 33.5, 19.5, 9.6, 10],
    'quantity': [100, 34, np.NaN, 56, 120]})
print(f'Сколько пропусков в датасете:\n{df.isnull().sum()}\n')
df = df.dropna(axis=0, how='any')
print(f'{df}\n')
df['total cost'] = [100 * 25, 34 * 33.5, 56 * 9.6, 120 * 10]
print(f'{df}\n')

df_1 = pd.DataFrame({
    'fruit': ['Apple', 'Melon', 'Peach'],
    'price': [25, 30, 98],
    'quantity': [100, 55, 11]})
df_1['total cost'] = [100 * 25, 55 * 30, 11 * 98]
df = pd.concat([df, df_1], ignore_index=True)
df = df.drop(0, axis=0)
print(df)
