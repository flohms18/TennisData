import pandas as pd

df = pd.read_csv('AptSeason/AtpSeason2024.csv')
df = df[df['winner_name'] == 'Rafael Nadal'] 

print(df)