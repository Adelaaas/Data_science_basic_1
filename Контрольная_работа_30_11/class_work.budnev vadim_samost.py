import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


df = pd.read_csv("E:\Вадим\ParisHousingClass (1).csv")
print("# 1. Считайте DataFrame")
print(df)
print("""# 2. Проведите анализ DataFrame
# - Какая размерность данных?
# - Какие типы переменных представленны в наборе данных?
# - Есть пропуски в данных? Если да, удалите строки, в которых есть пропуски""")
print()
print("Размерность данных")
print(df.shape)
print()
print("типы данных в таблице")
print(df.dtypes)
print()
print("пропуски в данных")
print('Пропуски, есть или нет, проверка')
print(df.isna().sum())
df.dropna(axis=1, how='any',inplace=True)
print(df)
print()
print("""# 3. Напишите функцию, которая принимает DataFrame, типо category
# и возвращает кортеж
# (средняя цена квартиры для этого типа category, max цену для этого типа category, min цену для этого типа category)""")
def dfF(df):
    a = df.loc[(df['category']=='Basic')]
    a1 = df.loc[(df['category']=='Luxury')]
    a_max = a['price'].max()
    a_min = a['price'].min()
    a_mean = a['price'].mean()
    a_max1 = a1['price'].max()
    a_min1 = a1['price'].min()
    a_mean1 = a1['price'].mean()
    return (a_max,a_min,a_mean,a_max1,a_min1,a_mean1)
print(dfF(df))
print("""# 6. Создайте новый столбец в DataFrame, в котором будут типы category будут заменены на числовые значения
# например, все значения Basic станут равны 0, Luxury = 1""")
df['New']=['0' if x=='Basic' else '1' for x in df['category']]
print(df)
print()
print("# 5. Удалите из набора данных все однокомнатные квартиры (numberOfRooms = 1) цена которых ниже 2 000 000")
a=[]
df1 = df.loc[(df['price']<2000000) & (df['numberOfRooms']==1)]
a.append(df1.index)
for i in range(len(a)):
    df.drop(index=a[i],inplace=True)
print(df)

print()
print("Задание номер 4")
print(""" 4. Постройте график:
# - гистограмма количества записей для каждого типа category
# - гистограмма средней цены для каждого типа category (пример приводится)

# Графики должны располагать на РАЗНЫХ координатных плоскостях
# У графика должен быть заголовок, подписаны оси, а также легенда (т е графики должны быть подписаны)""")
X = ['basic', 'luxury']
Y = [len(df[df['category'] == 'Basic']), len(df[df['category'] == 'Luxury'])]
fig, ax = plt.subplots()
ax.bar(X, Y)
plt.show()