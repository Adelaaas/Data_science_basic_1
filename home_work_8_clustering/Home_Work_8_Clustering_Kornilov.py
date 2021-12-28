import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("1. Загрузка датасета в датафрейм:")
df = pd.read_csv("C:/Users/danik/Downloads/CC GENERAL.csv")
print(f'\n{df}')
print('- ' * 40)

print("2. Исследование данных:")
print(f'размерность данных: {df.shape}')
print('- ' * 40)
print(f'типы переменных в данных:\n{df.dtypes}')
print('- ' * 40)
print(df.dropna(axis=0, inplace=True, how="any"))

# 3. Пункт
"""
BALANCE - баланс на карте клиента. Он позволяет понять покупательскую способность клиента.
PURCHASES_TRX - количество покупок.
PURCHASES - сумма покупок.
Исходя из этих параметров можно понять возможности и предпочтения клиента.
"""

print("4. Пункт: подбор числа кластеров при помощи метода локтя:")
Sum_of_squared_distances = []
for k in range(1, 15):
    kmeans = KMeans(n_clusters=k)
    kmeans = kmeans.fit(X=df.loc[:, ['BALANCE', 'PURCHASES', 'PURCHASES_TRX']])
    Sum_of_squared_distances.append(kmeans.inertia_)
plt.plot(range(1, 15), Sum_of_squared_distances, )
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

print("5. Пункт: разбивка объектов на кластеры с помощью метода kmeans и создание в датасете новой колонки, "
      "в которой записан кластер, в который попал наш клиент.\n")
kmeans = KMeans(n_clusters=9)
kmeans.fit(X=df.loc[:, ['BALANCE', 'PURCHASES', 'PURCHASES_TRX']])
Y_pred = kmeans.labels_
df['CLUSTER'] = Y_pred
X1 = df.loc[:, ['BALANCE', 'PURCHASES', 'PURCHASES_TRX', 'CLUSTER']]
print(X1)

print("6.Выберете любые два признака и проведите по ним кластеризацию, визуализируйте полученные кластеры")
X = df.loc[:, ['PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY']]
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
Y_pred = kmeans.labels_
df['CLUSTER_1'] = Y_pred
print(f'\n{df}\n')

X = df.loc[:, ['INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'CLUSTER_1']]
plt.plot(X[X['CLUSTER_1'] == 0]['INSTALLMENTS_PURCHASES'], X[X['CLUSTER_1'] == 0]['CASH_ADVANCE'], 'ro',
         label='class1')
plt.plot(X[X['CLUSTER_1'] == 1]['INSTALLMENTS_PURCHASES'], X[X['CLUSTER_1'] == 1]['CASH_ADVANCE'], 'go',
         label='class2')
plt.plot(X[X['CLUSTER_1'] == 2]['INSTALLMENTS_PURCHASES'], X[X['CLUSTER_1'] == 2]['CASH_ADVANCE'], 'bo',
         label='class3')
plt.plot(X[X['CLUSTER_1'] == 3]['INSTALLMENTS_PURCHASES'], X[X['CLUSTER_1'] == 3]['CASH_ADVANCE'], 'yo',
         label='class4')
plt.xlabel('PURCHASES_FREQUENCY')
plt.ylabel('ONEOFF_PURCHASES_FREQUENCY')
plt.legend(loc=0)
plt.show()
