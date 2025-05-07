import pandas as pd

psg_players = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'])
print(psg_players)

psg_players_index = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'],index =[1,7,10,30])
print(psg_players_index)

psg_players_dict = {1:'Navas', 7:'Mbappe',10:'Neymar',30:'Messi'}
print(pd.Series(psg_players_dict))

print(psg_players[0:3])

dict = { 'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
'Altura' :[183.0, 170.0, 170.0, 165.0],
'Goles': [2, 100, 200, 300] }

df_players = pd.DataFrame(dict)
print(df_players)
print(df_players.columns)