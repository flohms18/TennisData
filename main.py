import pandas as pd

df = pd.read_csv('AtpSeason2024.csv')['winner_name']

print(df)