import pandas as pd

P1Name = input("Write the Name for P1 ")
P2Name = input("Write the Name for P2 ")
TotalP1 = 0
TotalP2 = 0

for x in range(2000,2025):
    df = pd.read_csv('AptSeason/atp_matches_' + str(x) + '.csv')
    Nadal = df[(df['winner_name'] == P1Name) & (df['loser_name'] == P2Name)]
    Djokovic = df[(df['winner_name'] == P2Name) & (df['loser_name'] == P1Name)]
    if Nadal.values.any() == True or Djokovic.values.any() == True :

        CountP1 =+ len(Nadal)
        CountP2 =+ len(Djokovic)
        print(f"In {x} {P1Name} won {CountP1} times, {P2Name} won {CountP2} times !")
        TotalP1 += len(Nadal)
        TotalP2 += len(Djokovic)
print(f"{P1Name} won {TotalP1} times, while {P2Name} won {TotalP2} times !")


    