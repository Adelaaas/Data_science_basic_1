import numpy as np
import pandas as pd

print("Номер 1")
print("Задан Series объект s, найти индекс первого элемента отсортированного s, где значения больше 5.")
print()
r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
print(s.sort_values()[s>5][:1].index)

print()
print("Номер 2")
print(""""Имеется небольшой игрушечный DataFrame, в котором необходимо провести несколько типов фильтраций и отобразить результат:
всех, кто старше 40
всех, кто имеет доход выше среднего по датасету
всех, кто имеет доход выше среднего по датасету, но надежность ниже среднего по датасету
создать новые столбцы:
важность клиента = доход * надежность
возможная долгосрочность клиента = важность клиента * (средний возраст по датасету - возраст клиента)""")
print()

df = pd.DataFrame({
    'имя': ['Петя', 'Вася', 'Аня', 'Света'],
    'возраст': [45, 26, 41 , 21],
    'доход': [100000, 80000, 150000, 60000],
    'надежность клиента (0..1)': [0.65, 0.74, 0.87, 0.68],
    'пол': ['муж', 'муж', 'жен', 'жен']},
    index=[0, 1, 2, 3])
a = df["возраст"]>40
d = df['доход']>df['доход'].sum()/4
d1 = (df['доход']>df['доход'].sum()/4) & (df['надежность клиента (0..1)']<df['надежность клиента (0..1)'].mean())
print("кто старше 40")
print(df[a])
print()
print("кто имеет доход выше среднего по датасету")
print(df[d])
print()
print("кто имеет доход выше среднего по датасету, но надежность ниже среднего по датасету")
print(df[d1])
print()
print("важность клиента = доход * надежность")
df['важность клиента']=[100000 * 0.65, 80000 * 0.74, 150000 * 0.87, 60000 * 0.68]
print(df)
print()
print("возможная долгосрочность клиента = важность клиента * (средний возраст по датасету - возраст клиента)")
df['возможная долгосрочность клиента']=[100000 * 0.65*(df['возраст'].sum() / 4-45),
                                        80000 * 0.74*(df['возраст'].sum()/4-26),
                                        150000 * 0.87*(df['возраст'].sum()/4-41),
                                        60000 * 0.68*(df['возраст'].sum()/4-21)]
print(df)

print()
print("Номер 3")
print("""Как объединить два DataFrame по двум столбцам так, чтобы остались только общие строки?
Объедините df1 и df2 по столбцам fruit-frukt и weight-ves.""")
print()

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})
df1 = pd.concat([df1, df2], axis=0, join="outer", verify_integrity=True, ignore_index=True)
df1 = df1.drop(columns=['ves', 'frukt'], inplace=False)
print(df1.head(9))

print()
print("Номер 4")
print("""Имеется датафрейм со столбцами:

страна
население данной страны
площадь
1. Создайте новые столбцы, которые будут содержать:
Коды страны: 'KZ', 'RU', 'BY', 'UA'
Плотность населения = население (в миллионах) поделить на площадь страны

2. Добавьте в датафрейм данные еще о двух странах:
USA; 329,5; 9834
United Kingdom; 55,98; 130279

3. Найдите среднюю площадь всех стран""")

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
print("Пункт 1")
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628],
    'Kod country': ['KZ', 'RU', 'BY', 'UA'],
    'nasel':[ 17.04*1000000/2724902,
              143.5*1000000/17125191,
              9.5*1000000/207600,
              45.5*1000000/603628]})
print(df)
print("Пункт 2")
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine','Usa','UK'],
    'population': [17.04, 143.5, 9.5, 45.5,329.5,55.98],
    'square': [2724902, 17125191, 207600, 603628,9826630,130279],
    'Kod country': ['KZ', 'RU', 'BY', 'UA','US','GB'],
    'nasel':[ 17.04*1000000/2724902,
              143.5*1000000/17125191,
              9.5*1000000/207600,
              45.5*1000000/603628,
              329.5*1000000/9826630,
              55.98*1000000/130279]})
print(df)
print("Пункт 3")
print(df['square'].mean(),"Средняя площадь всех стран")