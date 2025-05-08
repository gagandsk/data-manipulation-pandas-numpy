import pandas as pd

df_books = pd.read_csv('bestsellers.csv', sep=',',header=0)
print(df_books.head())

#pivot
print(df_books.pivot_table(index='Author',columns='Genre',values='User Rating'))
print(df_books.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum'))

#melt
print(df_books[['Name','Genre']].head(5))
print(df_books[['Name','Genre']].head(5).melt())
print(df_books.melt(id_vars='Year',value_vars='Genre'))