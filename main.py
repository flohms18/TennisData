import pandas as pd

P1Name = input("Select P1")
P2Name = input("Select P2")

for x in range(2000,2025):
    df = pd.read_csv('AptSeason/atp_matches_' + str(x) + '.csv')
    Nadal = df[(df['winner_name'] == P1Name) & (df['loser_name'] == P2Name)]
    Djokovic = df[(df['winner_name'] == P2Name) & (df['loser_name'] == P1Name)]
    CountP1 =+ len(Nadal)
    CountP2 =+ len(Djokovic)
    print(f"In {x} {P1Name} won {CountP1} times, {P2Name} won {CountP2} times !")
print(CountP1)
print(CountP2)