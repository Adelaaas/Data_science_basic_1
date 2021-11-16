import pandas as pd

df = pd.read_csv("income_evaluation.csv", sep=',')

print(df['age'].sum() / len(df['age']))