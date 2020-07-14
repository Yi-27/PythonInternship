#coding:utf-8

import pandas as pd

x1 = {1: 106, 2: 3, 7: 42}
a = x1.keys()
b = x1.values()
df = pd.DataFrame([a,b],index=['type', 'cnt'])#创建dataframe
print(df)
df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)#转置
print(df2)