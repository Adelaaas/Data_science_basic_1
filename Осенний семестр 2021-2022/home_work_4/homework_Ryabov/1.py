import numpy as np
import pandas as pd

r = np.random.RandomState(1)
s = pd.Series(r.uniform(0, 10, 100))

s.sort_values(inplace=True)
print(s[s > 5].index[0])
