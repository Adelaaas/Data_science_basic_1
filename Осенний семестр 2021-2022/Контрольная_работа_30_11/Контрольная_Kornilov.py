import pandas as pd
import matplotlib.pyplot as plt

print("Задание 1: \n")
# 1. Считайте DataFrame

df = pd.read_csv("C:/Users/maryk/Downloads/new_train.csv/new_train.csv", encoding="utf-8")
print(f'{df}\n')
# --------------------------------------------------------
print("Задание 2: \n")
# 2. Проведите анализ DataFrame
# - Какая размерность данных?
# - Какие типы переменных представленны в наборе данных?
# - Есть пропуски в данных? Если да, удалите строки, в которых есть пропуски

a = df.shape
b = df.dtypes
print(f'{a} - shape\n{b}\n')
df.dropna(axis=0, how='any')
# --------------------------------------------------------
print("Задание 3: \n")
# 3. Напишите функцию, которая принимает DataFrame
# и заменяет все категории в loan на числовые значения (no = 0, yes = 1)
# а также вовзращает средний возраст для каждого типа loan

def fun(df):
    mid = df.groupby('loan').age.mean().to_dict()
    voc = {'no': 0, 'yes': 1, 'unknown': 2}
    df['loan'] = df['loan'].map(voc)
    return (mid)


n: int = 6
print(f'{fun(df)}\n')
print(df)
# --------------------------------------------------------
print("Задание 4: \n")
# 4. Постройте график:
# - гистограмма количества записей для каждого типа job
# - гистограмма среднего возраста для каждого типа job

# Графики должны располагать на РАЗНЫХ координатных плоскостях
# У графика должен быть заголовок, подписаны оси, а также легенда (т е графики должны быть подписаны)

print("Гистограммы\n")
df.groupby('job')['age'].nunique().plot(kind='bar', title='Гистограмма кол-ва записей для каждого типа job')
plt.show()

df.groupby('job')['age'].mean().plot(kind='bar', title='Гистограмма среднего возраста для каждого типа job')
plt.show()
# --------------------------------------------------------
print("Задание 5: \n")
# 5. Удалите из набора данных все данные для которых job = retired
# Посчитайте максимальный возраст для исходного датафрейма
# Посчитайте максимальный возраст после удаления строк job = retired

print(f'Макс возраст для исходного датафрейма = {df["age"].mean()}')
df1 = df[df['job'] != 'retired']
print(f'Макс возраст после удаления строк job = retired: {df1["age"].mean()}\n')
# --------------------------------------------------------

print("Задание 6: \n")
# 6. Создайте новый столбец - mean_age - в котором будет средний возраст для каждого типа marital
# пример:
# marital | mean_age |
#  single |    20    |
#  single |    20    |
# married |    30    |


voc_1 = {'married': df[df['marital'] == 'married'].age.mean(),
         'divorced': df[df['marital'] == 'divorced'].age.mean(),
         'single': df[df['marital'] == 'single'].age.mean()}
df["mean_age"] = df["marital"]
df["mean_age"] = df["mean_age"].map(voc_1)

print(df)
