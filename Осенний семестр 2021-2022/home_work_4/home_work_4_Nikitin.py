import pandas as pd
import numpy as np
# Задача 1
r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
print(s[s>5].index[0])
# Задача 2
df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41 , 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index = [0, 1, 2, 3])

age = df['возраст']>40
money = df['доход'] > df['доход'].sum()/4
r = df['надежность клиента (0..1)'] < df['надежность клиента (0..1)'].mean()
print(f'Старше 40:\n{df[age]}')
print(f'\n имеет доход выше среднего по датасету:\n{df[money]}')
print(f'\n имеет доход выше среднего по датасету, но надежность ниже среднего по датасету:\n{df[money&r]}')
df['важность']=[100000*0.65, 80000*0.74, 150000*0.87, 60000*0.68]
df['долгосрочность']=[100000*0.65*(45-df['возраст'].sum()/4), 80000*0.74*(26-df['возраст'].sum()/4), 150000*0.87*(41-df['возраст'].sum()/4), 60000*0.68*(21-df['возраст'].sum()/4)]
print(f'\n{df}')

# Задача 3
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})
df1 = pd.concat([df1, df2], axis=0, join="outer", ignore_index=True, verify_integrity=True)
df1 = df1.drop(columns=['ves', 'frukt'], inplace=False)
print(df1.head(9))

# Задача 4.1


# Задача 4.2


# Задача 4.3
