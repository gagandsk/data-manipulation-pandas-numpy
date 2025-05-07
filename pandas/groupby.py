import pandas as pd

df_books = pd.read_csv('bestsellers.csv', sep=',', header=0, names=['Name', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])
df_books.head(2)

print(df_books.groupby('Year').count())
# mean => media
#print(df_books.groupby('Year').mean())
#print(df_books.groupby('Year').min())
#print(df_books.groupby('Year').max())
#print(df_books.groupby('Year').sum())
#print(df_books.groupby('Year').sum().loc['William Davis'])
#df_books.groupby('Author').sum().reset_index()
print(df_books.groupby('Author').agg(['min', 'max']))

df_books.head(2)

print(df_books.groupby('Author').agg({'Reviews': ['min', 'max'], 'User Rating': 'sum'}))
print(df_books.groupby(['Author', 'Year']).count())