import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("C:/Users/danik/Downloads/CC GENERAL.csv")
print(f'{df}\n')

X = df.loc[:, ['BALANCE', 'PURCHASES', 'PURCHASES_TRX']]
Z = linkage(X, 'ward')
fig = plt.figure(figsize=(10, 10))
dn = dendrogram(Z)
plt.show()

# SkLearn
hc = AgglomerativeClustering(n_clusters=7, affinity='euclidean', linkage='ward')
y_hc = hc.fit_predict(X)
print(y_hc)

plt.scatter(X.loc[y_hc == 0, 'BALANCE'], X.loc[y_hc == 0, 'PURCHASES'], s=50, marker='o', color='cyan')
plt.scatter(X.loc[y_hc == 1, 'BALANCE'], X.loc[y_hc == 1, 'PURCHASES'], s=50, marker='o', color='black')
plt.scatter(X.loc[y_hc == 2, 'BALANCE'], X.loc[y_hc == 2, 'PURCHASES'], s=50, marker='o', color='red')
plt.scatter(X.loc[y_hc == 3, 'BALANCE'], X.loc[y_hc == 3, 'PURCHASES'], s=50, marker='o', color='green')
plt.scatter(X.loc[y_hc == 4, 'BALANCE'], X.loc[y_hc == 4, 'PURCHASES'], s=50, marker='o', color='orange')
plt.scatter(X.loc[y_hc == 5, 'BALANCE'], X.loc[y_hc == 5, 'PURCHASES'], s=50, marker='o', color='purple')
plt.scatter(X.loc[y_hc == 6, 'BALANCE'], X.loc[y_hc == 6, 'PURCHASES'], s=50, marker='o', color='gray')

plt.xlabel('BALANCE')
plt.ylabel('PURCHASES')
plt.legend(loc=0)
plt.show()

# SciPy
label = fcluster(Z, 75000, criterion='distance')
np.unique(label)

plt.scatter(X.loc[label == 1, 'BALANCE'], X.loc[label == 1, 'PURCHASES'], s=50, marker='o', color='blue')
plt.scatter(X.loc[label == 2, 'BALANCE'], X.loc[label == 2, 'PURCHASES'], s=50, marker='o', color='cyan')
plt.scatter(X.loc[label == 3, 'BALANCE'], X.loc[label == 3, 'PURCHASES'], s=50, marker='o', color='yellow')
plt.scatter(X.loc[label == 4, 'BALANCE'], X.loc[label == 4, 'PURCHASES'], s=50, marker='o', color='black')
plt.scatter(X.loc[label == 5, 'BALANCE'], X.loc[label == 5, 'PURCHASES'], s=50, marker='o', color='orange')
plt.scatter(X.loc[label == 6, 'BALANCE'], X.loc[label == 6, 'PURCHASES'], s=50, marker='o', color='gray')
plt.scatter(X.loc[label == 7, 'BALANCE'], X.loc[label == 7, 'PURCHASES'], s=50, marker='o', color='purple')

plt.xlabel('BALANCE')
plt.ylabel('PURCHASES')
plt.legend(loc=0)
plt.show()
