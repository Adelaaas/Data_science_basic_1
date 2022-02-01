import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("income_evaluation.csv", sep=',')

x = ['Мужчины', 'Женщины']
y = [len(df[df[' sex'] == ' Male']), len(df[df[' sex'] == ' Female'])]

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('black')
fig.set_facecolor('floralwhite')

plt.show()