import pandas as pd
import numpy as np

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['low', 'medium', 'high'] * 3,
                    'price': np.random.randint(0, 100, 9)})

df2 = pd.DataFrame({'frukt': ['apple', 'banana', 'melon'] * 2,
                    'ves': ['low', 'high'] * 3,
                    'price': np.random.randint(0, 100, 6)})

print(df1)
print()
print(df2)
print()


df1.merge(df2, how='inner', left_on=['fruit', 'weight'], right_on=['frukt', 'ves'])
print(df1)
