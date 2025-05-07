import pandas as pd

df_books = pd.read_csv('bestsellers.csv', sep=',', header=0, names=['Name', 'Author', 'User Rating', 'Review', 'Price', 'Year', 'Genre'])
df_books.head(2)

print(df_books.info())
print(df_books.describe())

#me devuelve las 'n' ultimas filas
print(df_books.tail(2))

#me devuelve las 'n' primeras filas
print(df_books.head(2))

print(df_books.memory_usage(deep=True))

print(df_books['Author'].value_counts())

print(df_books.iloc[0])

df_books = df_books._append(df_books.iloc[0])
print(df_books)

df_books.drop_duplicates(keep='last')
print(df_books)

print(df_books.sort_values('Year'))
print(df_books.sort_values('Year', ascending=False))