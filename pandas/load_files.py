import pandas as pd

url = "https://static.platzi.com/media/public/uploads/hpcharactersdataraw_3d934e85-dfa4-42ec-8520-fadfbecae574.json"

df_books = pd.read_csv('bestsellers.csv', sep=',', header=0, names=['Names', 'Authors', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])
print(df_books)

print("---> JSON <--- ")
print(pd.read_json('HPCharactersData.json', typ='Series'))