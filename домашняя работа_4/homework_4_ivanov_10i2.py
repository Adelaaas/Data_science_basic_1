
#1
import numpy as np
import pandas as pd
r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
f = s[s>5].index[0]
print(f)
#2
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
earn = df[df['доход'] > averege]

trust = df['надежность клиента '].mean()
df[(df['доход'] > averege) & (df['надежность клиента '] < trust)]

df['важность клиента'] = df['доход'] * df['надежность клиента ']
df['возможная долгосрочность клиента'] = df['важность клиента'] * df['возраст'].mean()
df
#3
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})
#4.1
import pandas as pd

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})

df
