# -*- coding: utf-8 -*-
"""home_work_4_ivanov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zf0pDITblJ4xc1VAs9Sqjs9qLVFjPAmR
"""

import pandas as pd

"""Number 1"""

import numpy as np
import pandas as pd

r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))

d = s.index

s

"""Number 2"""

df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41 , 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])

age = df[df['возраст'] > 40]
sum = 0
averege = df['доход'].mean()

trust = df['надежность клиента (0..1)'].mean()
df[(df['доход'] > averege) & (df['надежность клиента (0..1)'] < trust)]

df['важность клиента'] = df['доход'] * df['надежность клиента (0..1)']
df['возможная долгосрочность клиента'] = df['важность клиента'] * df['возраст'].mean()
df