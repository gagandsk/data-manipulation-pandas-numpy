import pandas as pd
import numpy as np

df_books = pd.read_csv('bestsellers.csv', sep=',', header=0)
df_books.head(2)


print(df_books.drop('Genre', axis=1, inplace=True))
df_books.head(2)

print(df_books.drop('Year', axis=1))
df_books.head(2)

del df_books['Price']

# Delete columns
df_books.head(2)
print(df_books.drop(0, axis=0).head(2))

print(df_books.drop([0,1,2], axis=0).head(2))

# delet rows
print(df_books.drop(range(0,10), axis=0).head(2))

df_books.head(2)
df_books['New Column'] = np.nan
print(df_books)
df_books.head(2)

data = np.arange(0, df_books.shape[0])
print(data)

df_books['Range'] = data

print(df_books)

# Add Rows
df_books._append(df_books) # df_books.append(df_books)
print(df_books)