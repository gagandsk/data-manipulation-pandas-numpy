import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
 'B': ['B0', 'B1', 'B2', 'B3'],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
 'B': ['B4', 'B5', 'B6', 'B7'],
 'C': ['C4', 'C5', 'C6', 'C7'],
 'D': ['D4', 'D5', 'D6', 'D7']})

print(df1)
print(df2)

print(pd.concat([df1, df2], ignore_index=True))
print(pd.concat([df1, df2], axis=1))

#merge
left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
 'A': ['A0', 'A1', 'A2', 'A3'],
 'B': ['B0', 'B1', 'B2', 'B3'],})

right = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3'],})

print(left.merge(right, on='key'))



left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
 'A': ['A0', 'A1', 'A2', 'A3'],
 'B': ['B0', 'B1', 'B2', 'B3'],})

right = pd.DataFrame({'key_2': ['k0', 'k1', 'k2', 'k3'],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3'],})

#print(left.merge(right, on='key')) # error -> no hay match de keys
print(left.merge(right, left_on='key', right_on='key_2'))

left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
 'A': ['A0', 'A1', 'A2', 'A3'],
 'B': ['B0', 'B1', 'B2', 'B3'],})

right = pd.DataFrame({'key_2': ['k0', 'k1', 'k2', np.nan],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3'],})

print(right)

print('how: inner =>\n', left.merge(right, left_on='key', right_on='key_2', how='inner'))
print('how: left =>\n', left.merge(right, left_on='key', right_on='key_2', how='left'))
print('how:right =>\n', left.merge(right, left_on='key', right_on='key_2', how='right'))