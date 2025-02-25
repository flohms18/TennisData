import pandas as pd

df = pd.read_csv('AptSeason/AtpSeason2024.csv')['winner_name']

print(df)