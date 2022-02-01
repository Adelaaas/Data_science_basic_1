import pandas as pd

df = pd.read_csv("income_evaluation.csv", sep=',')

types = set(df[' education'])

answ = dict()

for i in types:
    answ[i] = 0

for i in (df[' education']):
    answ[i] += 1

print(answ)
