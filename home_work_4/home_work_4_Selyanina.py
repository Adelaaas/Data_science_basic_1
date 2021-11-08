# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wURrrsa0uUpXQ-9x36f6DKTeaqCR-OCw

Задан Series объект s, найти индекс первого элемента отсортированного s, где значения больше 5.
"""

# 1
import numpy as np
import pandas as pd

r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
s = s.sort_values()
print(s[s > 5].index[0])

"""Имеется небольшой игрушечный DataFrame, в котором необходимо провести несколько типов фильтраций и отобразить результат:

всех, кто старше 40
всех, кто имеет доход выше среднего по датасету
всех, кто имеет доход выше среднего по датасету, но надежность ниже среднего по датасету
создать новые столбцы:

важность клиента = доход * надежность
возможная долгосрочность клиента = важность клиента * (средний возраст по датасету - возраст клиента)
"""
#2
import numpy as np
import pandas as pd
df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41, 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])
age = df['возраст'] > 40
#print(f'Старше 40:\n{df[age]}')
money = df['доход'] > df['доход'].sum() / 4
#print(f'\n имеет доход выше среднего по датасету:\n{df[money]}')
relible = df['надежность клиента (0..1)'] < df['надежность клиента (0..1)'].mean()
#print(f'\nимеет доход выше среднего по датасету, но надежность ниже среднего по датасету:\n{df[money & relible]}')
df['важность клиента'] = [100000 * 0.65, 80000 * 0.74, 150000 * 0.87, 60000 * 0.68]
df['возможная долгосрочность клиента'] = [100000 * 0.65 * (45 - df['возраст'].sum() / 4),
                                          80000 * 0.74 * (26 - df['возраст'].sum() / 4),
                                          150000 * 0.87 * (41 - df['возраст'].sum() / 4),
                                          60000 * 0.68 * (21 - df['возраст'].sum() / 4)]

df

"""Как объединить два DataFrame по двум столбцам так, чтобы остались только общие строки?

Объедините df1 и df2 по столбцам fruit-frukt и weight-ves.

"""
#3
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})

# ваш код тут

pd.concat([df1, df2], axis=1)
df1

"""1. Создайте новые столбцы, которые будут содержать:

Коды страны: 'KZ', 'RU', 'BY', 'UA'
Плотность населения = население (в миллионах) поделить на площадь страны
2. Добавьте в датафрейм данные еще о двух странах:

USA; 329,5; 9834
United Kingdom; 55,98; 130279
3. Найдите среднюю площадь всех стран

"""
#4
import pandas as pd

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine', 'USA', 'United Kingdom'],
    'population': [17.04, 143.5, 9.5, 45.5, 329.5, 55.98],
    'square': [2724902, 17125191, 207600, 603628, 9834, 130279]})
df['Коды страны:'] =  'KZ', 'RU', 'BY', 'UA', 'USA', 'UK' 
#print(df)
#money = df['доход'] > df['доход'].sum() / 4
pl = df['population']/df['square']
df['Плотность населения'] = pl
AllSquare = df['square'].sum() / 6
#df['Средняя площадь всех стран'] = AllSquare

df['Средняя площадь всех стран'] = AllSquare
df