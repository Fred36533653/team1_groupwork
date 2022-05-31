import logging

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

print(df)

# 선택한 셀의 행과 열이 모두 일대일대응이 되도록...
import itertools

nums = [i for i in range(n)]
permuatation = itertools.permutations(nums)
permuatation_list = [i for i in permuatation]


def fac(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * fac(n - 1)


from collections import deque

list_basic = deque()
for i in range(n):
    list_basic.append(i)

list_rot = [deque(permuatation_list[i]) for i in range(fac(n - 1))]

index_list = []
for i in range(fac(n - 1)):
    for j in range(n):
        a = list(zip(list_basic, list_rot[i]))
        index_list.append(a)
        list_rot[i].rotate(-1)


# 최솟값을 가지는 솔루션과 그때 셀의 위치를 반환하는 함수
def result():
    sum_list = []
    for i in range(len(index_list)):
        c = []
        for j in range(n):
            a = df.iloc[index_list[i][j][0], index_list[i][j][1]]
            c.append(a)
        sum_list.append(sum(c))
    value = min(sum_list)

    for i in range(len(sum_list)):
        if sum_list[i] == value:
            return index_list[i], value
        else:
            pass


position = result()[0]
min_value = result()[1]

print(position)
print(min_value)

# 결과를 데이터 프레임으로 반환
row_ind = ['기계 {}'.format(i + 1) for i in range(n)]
col_ind = ['작업 {}'.format(position[i][1] + 1) for i in range(n)]

b = []
for i in range(n):
    b.append([row_ind[i], col_ind[i]])

ans = pd.DataFrame(b)
print(ans)

# 솔루션을 출력 파일에 저장
path_write = 'team01_groupwork/output/result.csv'
ans.to_csv(path_write, index = False, header = False)