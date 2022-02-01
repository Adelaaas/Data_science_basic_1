import numpy as np
import pandas as pd

r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
s=s.sort_values()
print(s[s>5].index[0])
print("\n")
df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41 , 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])
print(df[df['возраст'] > 40])
print("\n")
print(df[(df['доход']>df['доход'].sum()/4)])
print("\n")
print(df[(df['доход']>df['доход'].sum()/4) & (df['надежность клиента (0..1)']<df['надежность клиента (0..1)'].sum()/4)])
print("\n")
df['важность клиента']=[100000*0.65,80000*0.74,150000*0.87,60000*0.68]
df['возможная долгосрочность клиента']=[100000*0.65*(df['возраст'].sum()/4-45),80000*0.74*(df['возраст'].sum()/4-26),150000*0.87*(df['возраст'].sum()/4-41),60000*0.68*(df['возраст'].sum()/4-21)]
print(df)
print("\n")
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})
df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})
g = pd.merge(df1, df2, how='inner', left_on=['fruit', 'weight'], right_on=['frukt', 'ves'], suffixes=['_1', '_2'])
print(g)
print("\n")

df3 = pd.DataFrame({
    'fruit': ['Apple', 'Watermelon', 'Cherry', 'Orange', 'Banana'],
    'price': [25, 33.5, 19.5, 9.6, 10],
    'quantity': [100, 34, np.NaN, 56, 120]})
df3=df3.dropna(axis=0,how='any')
df3['общая стоимость']=[25.0*100.0,33.5*34.0,9.6*56.0,10.0*120.0]
print(df3)
df4=pd.DataFrame({
	'fruit':['Apple','Melon','Peach'],
	'price':[25,30,98],
	'quantity': [100,55,11]
})
df4=df4.drop([0])
df4['общая стоимость']=[55*30,98*11]
s=pd.concat([df3,df4],ignore_index=True)
print("\n",s)