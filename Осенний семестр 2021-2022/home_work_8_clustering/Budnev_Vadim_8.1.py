import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


print("Считайте DataFrame")
df = pd.read_csv("E:\Вадим\Wine.csv")
print(df)

print("2")
print(df.shape)
print(df.dtypes)
df = df.dropna()
print(df)
print()

print("3")
X = df.loc[:,['Flavanoids', 'OD280']]
print(X)


print("4")

SSE = []
for k in range(1, 9):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    SSE.append(kmeans.inertia_)

plt.plot(range(1, 9), SSE, marker='s');
plt.xlabel('k')
plt.ylabel('SSE');
plt.show()
print()

print("5")
kmeans = KMeans(n_clusters = 3)
kmeans.fit(X)
Y_pred = kmeans.labels_
print(Y_pred)

plt.scatter(df['Flavanoids'],df['OD280'])
plt.xlabel('Flavanoids')
plt.ylabel('OD280')
plt.show()

X['cluster'] = Y_pred
print(X)
print()

print("6")
plt.plot(X[X['cluster']==0]['Flavanoids'], X[X['cluster']==0]['OD280'], 'bo', label='class1')
plt.plot(X[X['cluster']==1]['Flavanoids'], X[X['cluster']==1]['OD280'], 'go', label='class2')
plt.plot(X[X['cluster']==2]['Flavanoids'], X[X['cluster']==2]['OD280'], 'ro', label='class3')
plt.xlabel('Flavanoids')
plt.ylabel('OD280')
plt.legend(loc=0)
plt.show()