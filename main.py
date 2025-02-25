import pandas as pd

year = input("Select year to analyse please: YYYY ")

df = pd.read_csv('AptSeason/atp_matches_' + year + '.csv')

rg = df[df['tourney_name'] == 'Roland Garros']



print(rg)