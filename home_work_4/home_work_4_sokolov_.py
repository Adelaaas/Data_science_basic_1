import numpy as np
import pandas as pd

print('\nЗадание 1')
r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
s = s.sort_values()
print(s[s > 5][:1])


print('\nЗадание 2')
df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41, 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])

age = df['возраст'] > 40
print(f'Старше 40:\n{df[age]}')

income = df['доход'] > df['доход'].sum() / 4
print(f'\nимеет доход выше среднего по датасету:\n{df[income]}')

reliability = df['надежность клиента (0..1)'] < df['надежность клиента (0..1)'].mean()
print(f'\nимеет доход выше среднего по датасету, но надежность ниже среднего по датасету:\n{df[income & reliability]}')

df['важность клиента'] = [100000 * 0.65, 80000 * 0.74, 150000 * 0.87, 60000 * 0.68]
df['возможная долгосрочность клиента'] = [100000 * 0.65 * (45 - df['возраст'].sum() / 4),
                                          80000 * 0.74 * (26 - df['возраст'].sum() / 4),
                                          150000 * 0.87 * (41 - df['возраст'].sum() / 4),
                                          60000 * 0.68 * (21 - df['возраст'].sum() / 4)]

print(f'\n{df}')

print('\nЗадание 3')
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})

df1 = pd.concat([df1, df2], axis=0, join="outer", verify_integrity=True, ignore_index=True)
df1 = df1.drop(columns=['ves', 'frukt'], inplace=False)
print(df1.head(9))


print('\nЗадание 4.3')

print('основа:')
df = pd.DataFrame({
    'name': ['Иван', 'Анна', 'Мария', 'Василий', 'Анастасия'],
    'math': [5, 3, 3, 4, 4],
    'russian': [4, 4, 4, 5, 3],
    'history': [5, 4, 3, 4, 5]})
print(df)

print('\nпункт 1:')
df_1 = pd.DataFrame({
    'name': ['Иван', 'Анна', 'Мария', 'Василий', 'Анастасия'],
    'class': ['11A', '11А', '11Б', '11Г', '11Б'],
    'math': [5, 3, 3, 4, 4],
    'russian': [4, 4, 4, 5, 3],
    'history': [5, 4, 3, 4, 5],
    'mean': [4.6, 3.6, 3.3, 4.3, 4.0]})
print(df_1)

print('\nпункт 2:')
df_1 = pd.DataFrame({
    'name': ['Иван', 'Анна', 'Мария', 'Василий', 'Анастасия'],
    'class': ['11A', '11А', '11Б', '11Г', '11Б'],
    'math': [5, 3, 3, 4, 4],
    'russian': [4, 4, 4, 5, 3],
    'history': [5, 4, 3, 4, 5],
    'mean': [4.6, 3.6, 3.3, 4.3, 4.0]})
df_1.drop(4, axis=0, inplace=True)
print(df_1)

print('\nпункт 3:')
df = pd.DataFrame({
    'name': ['Иван', 'Анна', 'Мария', 'Василий', 'Анастасия'],
    'math': [5, 3, 3, 4, 4],
    'russian': [4, 4, 4, 5, 3],
    'history': [5, 4, 3, 4, 5]})
print(f'{df.iloc[0]}\n', f'\n{df.iloc[3]}')