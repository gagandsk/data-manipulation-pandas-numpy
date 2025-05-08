import pandas as pd

df_books = pd.read_csv('bestsellers.csv', sep=',',header=0)
df_books.head(2)

def two_times(value):
    return value * 2

df_books['Rating_2'] = df_books['User Rating'].apply(two_times)
df_books['Rating_2_lambda'] = df_books['User Rating'].apply(lambda x: x * 3)
print(df_books['Rating_2'])
df_books.head(2)
print(df_books['Rating_2_lambda'])

df_books['Rating_2'] = df_books.apply(lambda x: x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1)
print(df_books['Rating_2'])