import pandas as pd

url = "https://static.platzi.com/media/public/uploads/hpcharactersdataraw_3d934e85-dfa4-42ec-8520-fadfbecae574.json"

df_books = pd.read_csv('bestsellers.csv', sep=',', header=0, names=['Name', 'Author', 'User Rating', 'Review', 'Price', 'Year', 'Genre'])
print(df_books)

print("---> JSON <--- ")
print(pd.read_json('HPCharactersData.json', typ='Series'))

print(df_books[0:4])
print(df_books['Name'])
print(df_books[['Name', 'Author', 'Year']])

#loc
print(df_books.loc[:])
print(df_books.loc[0:4])
print(df_books.loc[0:2, ['Name', 'Author']])
print(df_books.loc[:, ['Review']] * -1)
print(df_books.loc[0:2, ['Author']] == 'JJ Smith')

#iloc
print('\n ---> ILOC <--- \n')
print(df_books.iloc[:])
print(df_books.iloc[:, 0:3])
print(df_books.iloc[1:3] * -2)
print(df_books.iloc[:2, 2:])