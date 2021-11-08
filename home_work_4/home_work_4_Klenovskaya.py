import numpy as np
import pandas as pd
print('number 1')
r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))
s=s.sort_values()
print(f'{s[s>5][:1]}\n')

print('number 2')
df = pd.DataFrame({
    '���': ['����', '����', '���', '�����'],
    '�������': [45, 26, 41 , 21],
    '�����': [100000, 80000, 150000, 60000],
    '���������� ������� (0..1)': [0.65, 0.74, 0.87, 0.68],
    '���': ['���', '���', '���', '���']},
    index=[0, 1, 2, 3])
age = df['�������']>40
received_money = df['�����']>df['�����'].sum()/4
reliability = df['���������� ������� (0..1)']<df['���������� ������� (0..1)'].mean()
print(f'������ 40:\n{df[age]}')
print(f'\n ����� ����� ���� �������� �� ��������:\n{df[received_money]}')
print(f'\n ����� ����� ���� �������� �� ��������, �� ���������� ���� �������� �� ��������:\n{df[received_money&reliability]}')
df['�������� �������']=[100000*0.65, 80000*0.74, 150000*0.87, 60000*0.68]
df['��������� �������������� �������']=[100000*0.65*(45-df['�������'].sum()/4),
                                        80000*0.74*(26-df['�������'].sum()/4),
                                        150000*0.87*(41-df['�������'].sum()/4),
                                        60000*0.68*(21-df['�������'].sum()/4)]
print(f'\n{df}')

print('number 3')
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})
df1 = pd.concat([df1, df2], axis=0, join="outer", ignore_index=True, verify_integrity=True)
df1 = df1.drop(columns=['ves', 'frukt'], inplace=False)
print(df1.head(9))


print('number 4.2')
df = pd.DataFrame({
    'fruit': ['Apple', 'Watermelon', 'Cherry', 'Orange', 'Banana'],
    'price': [25, 33.5, 19.5, 9.6, 10],
    'quantity': [100, 34, np.NaN, 56, 120]})
print(f'������� ��������� � ��������:\n{df.isna().sum()}\n')
df=df.dropna(axis=0, how='any')
print(f'{df}\n')
df['total_fruit_cost']=[100*25, 34*33.5, 56*9.6, 120*10]
print(f'{df}\n')

df1= pd.DataFrame({
    'fruit': ['Apple', 'Melon', 'Peach'],
    'price': [25, 30, 98],
    'quantity': [100, 55, 11]})
df1['total_fruit_cost']=[100*25, 55*30, 11*98]
df=pd.concat([df, df1], ignore_index=True)
df=df.drop(0, axis=0)
print(df)