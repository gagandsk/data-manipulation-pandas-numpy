import pandas as pd

df_books = pd.read_csv('bestsellers.csv', sep=',', header=0, names=['Name', 'Author', 'User Rating', 'Review', 'Price', 'Year', 'Genre'])
df_books.head(2)

mayor_a_2016 = df_books['Year'] > 2016
print(mayor_a_2016)

print(df_books[mayor_a_2016])

genre = df_books['Genre'] == 'Fiction'
print(df_books[genre & mayor_a_2016])

# negacion
print(df_books[~mayor_a_2016])