import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering


print("Считайте DataFrame")
df = pd.read_csv("E:\Вадим\Wine.csv")
print(df)

X = df.iloc[:,:-1]
print(X)


Z = linkage(X, 'ward')
fig = plt.figure(figsize=(10, 10))
dn = dendrogram(Z)
plt.show()

Z = linkage(X, method='average', metric='euclidean')
print(Z[0])
print()

label = fcluster(Z, 1000, criterion='distance')
np.unique(label)
print(label)
print()

plt.scatter(df.loc[label==1, 'Alcohol'], df.loc[label==1, 'Proline'], s=50, marker='o', color='red')
plt.scatter(df.loc[label==2, 'Alcohol'], df.loc[label==2, 'Proline'], s=50, marker='o', color='blue')
plt.scatter(df.loc[label==3, 'Alcohol'], df.loc[label==3, 'Proline'], s=50, marker='o', color='green')
plt.scatter(df.loc[label==4, 'Alcohol'], df.loc[label==4, 'Proline'], s=50, marker='o', color='black')
plt.xlabel('Alcohol')
plt.ylabel('Proline')
plt.show()


hc = AgglomerativeClustering(n_clusters = 4, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)
X['pred_sklearn'] = y_hc
print(y_hc)
print()

plt.scatter(X.loc[label==1, 'Alcohol'], X.loc[label==1, 'Proline'], s=50, marker='o', color='black')
plt.scatter(X.loc[label==2, 'Alcohol'], X.loc[label==2, 'Proline'], s=50, marker='o', color='green')
plt.scatter(X.loc[label==3, 'Alcohol'], X.loc[label==3, 'Proline'], s=50, marker='o', color='blue')
plt.scatter(X.loc[label==4, 'Alcohol'], X.loc[label==4, 'Proline'], s=50, marker='o', color='red')
plt.xlabel('Alcohol')
plt.ylabel('Proline')
plt.show()