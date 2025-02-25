import pandas as pd

year = input("Select year to analyse please: YYYY ")

df = pd.read_csv('AptSeason/atp_matches_' + year + '.csv')

Nadal = df[(df['winner_name'] == 'Rafael Nadal') & (df['loser_name'] == 'Novak Djokovic')]
Djokovic = df[(df['winner_name'] == 'Novak Djokovic') & (df['loser_name'] == 'Rafael Nadal')]

print("Nadal won ! " + Djokovic['score'])
print("Djokovic won ! " + Djokovic['score'])