import pandas as pd
import matplotlib.pyplot as plt

print("\nЗадание 1: \n")
# 1. Считайте DataFrame

df = pd.read_csv("C:/Users/User/Downloads/archive (1).zip", encoding="utf-8")
print(df)

print("\nЗадание 2: \n")
# 2. Проведите анализ DataFrame
# - Какая размерность данных?
# - Какие типы переменных представленны в наборе данных?
# - Есть пропуски в данных? Если да, удалите строки, в которых есть пропуски

print(df.shape)
print("_" * 30)
print(df.dtypes)
print("_" * 30)
df.dropna(axis=0, how="any")

print("\nЗадание 3: \n")
# 3. Создайте функцию, которая принимает DataFrame, тип brand
# и возвращает словарь
# {'brand': название бренда, 'mean_price': ср. цена этого типа бренда, 'max_price': максимальна цена, 'min_price': минимальная цена}


def func(df):
    df_dict = df.groupby('brand')['price'].agg(['mean', 'max', 'min']).to_dict()
    return df_dict


print(func(df))

print("\nЗадание 4: \n")
# 4. Постройте график:
# - гистограмма количества записей для каждого типа country
# - гистограмма средней цены для каждого типа Brand

# Графики должны располагать на РАЗНЫХ координатных плоскостях
# У графика должен быть заголовок, подписаны оси, а также легенда (т е графики должны быть подписаны)

x = ['usa']
y = [len(df[df['country'] == 'usa'])]
n_1, n_2 = plt.subplots()
n_2.bar(x, y)
n_2.set_facecolor('red')
n_1.set_facecolor('white')
plt.title("Гистограмма количества записей для каждого типа country")
plt.show()

df.groupby('brand')['price'].mean().plot(kind='bar', title='Гистограмма средней цены для каждого типа brand')
plt.show()

print("\nЗадание 5: \n")
# 5. Создайте два новых столбца в датафрейм
# - days, в который будут записаны числа из condition
# (например, для 10 days left будет записано 10, а для 22 hours left - будет записано 0)

# - hours, в который будут записаны числа из condition
# (например, для 10 days left будет записано 0, а для 22 hours left - будет записано 22)

df['days'] = [x[:2].replace(' ', '') if 'days left' in x else '0' for x in df['condition']]
df['hours'] = ['0' if 'days left' in x else x[:2].replace(' ', '') for x in df['condition']]
print(df)
print()

print("\nЗадание 6: \n")
# 6. Удалите из датафрейма все строки где автомобили старше 2010 года, но только для тех
# штатов которые наборе встречаются чаще чем 100

a = []
df1 = df.loc[(df['year'] > 2010) & (df['state'] == 'illinois')]
df2 = df.loc[(df['year'] > 2010) & (df['state'] == 'minnesota')]
df3 = df.loc[(df['year'] > 2010) & (df['state'] == 'north carolina')]
df4 = df.loc[(df['year'] > 2010) & (df['state'] == 'michigan')]
df5 = df.loc[(df['year'] > 2010) & (df['state'] == 'california')]
df6 = df.loc[(df['year'] > 2010) & (df['state'] == 'texas')]
df7 = df.loc[(df['year'] > 2010) & (df['state'] == 'florida')]
df8 = df.loc[(df['year'] > 2010) & (df['state'] == 'pennsylvania')]

a.append(df1.index)
a.append(df2.index)
a.append(df3.index)
a.append(df4.index)
a.append(df5.index)
a.append(df6.index)
a.append(df7.index)
a.append(df8.index)

for i in range(len(a)):
    df.drop(index=a[i], inplace=True)

print(df)
print(df[['state', 'year']])
