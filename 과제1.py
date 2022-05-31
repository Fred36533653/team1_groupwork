# 역할 1
n = int(input("숫자를 입력하세요: "))

import pandas as pd
import numpy as np

a = []
column_name = []
row_name = []
index = range(n)
index_a = {}

random_list = range(1, 101)
for i in range(n):
    a.append([])

for i in range(n):
    for j in range(n):
        a[i].append(np.random.choice(random_list))

for i in range(n):
    column_name.append("작업 {}".format(i + 1))

for i in range(n):
    row_name.append("기계 {}".format(i + 1))
for i, v in enumerate(row_name):
    before = index[i]
    index_a[before] = v

df = pd.DataFrame(a)
df.columns = column_name
df.rename(index=index_a, inplace=True)

df