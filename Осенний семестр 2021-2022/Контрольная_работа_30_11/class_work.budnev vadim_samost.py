import pandas as pd
import matplotlib.pyplot as plt

print("1. Считайте DataFrame")
df = pd.read_csv("E:\Вадим\weatherAUS.csv")
print(df)
print(""" 3. Постройте график:
# - гистограмма количества записей для каждого типа Location
# - гистограмма количества записей для каждого типа WindDir9am	
# Графики должны располагать на РАЗНЫХ координатных плоскостях
# У графика должен быть заголовок, подписаны оси, а также легенда (т е графики должны быть подписаны)""")
y = []
x = []
for i in df['Location'].unique():
    x = x + [i]
for i in pd.unique(df['Location']).tolist():
    y += [len(df[df['Location'] == i])]
fig, ax = plt.subplots()
ax.bar(x, y)
plt.title('Тип Location')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

x = ['N','SE','E','SSE','NW','S','W','SW',
     'NNE','NNW','ENE','NE','ESE','SSW','WNW','WSW',]
y = [len(df[df['WindDir9am'] == 'N']),
     len(df[df['WindDir9am'] == 'sE']),
     len(df[df['WindDir9am'] == 'E']),
     len(df[df['WindDir9am'] == 'SSE']),
     len(df[df['WindDir9am'] == 'NW']),
     len(df[df['WindDir9am'] == 'S']),
     len(df[df['WindDir9am'] == 'W']),
     len(df[df['WindDir9am'] == 'SW']),
     len(df[df['WindDir9am'] == 'NNE']),
     len(df[df['WindDir9am'] == 'NNW']),
     len(df[df['WindDir9am'] == 'ENE']),
     len(df[df['WindDir9am'] == 'NE']),
     len(df[df['WindDir9am'] == 'ESE']),
     len(df[df['WindDir9am'] == 'SSW']),
     len(df[df['WindDir9am'] == 'WNW']),
     len(df[df['WindDir9am'] == 'WSW'])]
fig, ax = plt.subplots()
ax.bar(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Тип WindDir9am')
plt.show()



print()
print("""# 4. Напишите функцию, которая принимает DataFrame, дату начала, дату окончания
которая возвращает распределение кол-ва записей для каждого типа Location, RainToday, RainTomorrow
для выбранного временного диапазона
# ваш код тут""")
def adc(df,st,en):
    a = df.loc[(df['Date'] == st)]
    b = df.loc[(df['Date'] == en)]
    print("Location=st")
    print(a['Location'])
    print("Location=en")
    print(b['Location'])
    print("RainToday=st")
    print(a['RainToday'])
    print("RainToday=st=en")
    print(b['RainToday'])
    print("RainTomorrow=st")
    print(a['RainTomorrow'])
    print("RainTomorrow=en")
    print(b['RainTomorrow'])
    return
adc(df,st=input(),en=input())
print("""# 6. Создайте новую колонку в DataFrame - mean_Temp - в которой будет среднее значение по столбцам MinTemp	MaxTemp
# ваш код тут""")
df['mean_Temp']=df.groupby('MinTemp')['MaxTemp'].mean()
print(df)

print()
print("""# 5. Удалите из датафрейма строки для которых
# location = Canberra, Sydney, Adelaide, Darwin, Brisbane""")
a = df.loc[(df['Location']=='Canberra')]
df.drop(index=a.index,inplace=True)
b = df.loc[(df['Location']=='Sydney')]
df.drop(index=b.index,inplace=True)
c = df.loc[(df['Location']=='Adelaide')]
df.drop(index=c.index,inplace=True)
d = df.loc[(df['Location']=='Darwin')]
df.drop(index=d.index,inplace=True)
e = df.loc[(df['Location']=='Brisbane')]
df.drop(index=e.index,inplace=True)
print(df)
print()
print("""2. Проведите анализ DataFrame
# - Какая размерность данных?
# - Какие типы переменных представленны в наборе данных?
# - Есть пропуски в данных? Если да, удалите строки, в которых есть пропуски""")
print(df.shape)
print(df.dtypes)
b = df.isna().sum().sum()
if b>0:
    df.dropna(axis=1, how='any',inplace=True)
print(df)
print()