import numpy as np

# a = np.randn()
# print(a)

# a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
# print(np.sort(a))

a = np.array([ [[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]] ])
print(a)

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得資料集
df = sns.load_dataset('titanic')