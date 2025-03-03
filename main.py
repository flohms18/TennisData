import pandas as pd

P1Name = input("Write the Name for P1 ")
P2Name = input("Write the Name for P2 ")
TotalP1 = 0
TotalP2 = 0

for x in range(2000,2025):
    df = pd.read_csv('AptSeason/atp_matches_' + str(x) + '.csv')
    Player1 = df[(df['winner_name'] == P1Name) & (df['loser_name'] == P2Name)]
    Player2 = df[(df['winner_name'] == P2Name) & (df['loser_name'] == P1Name)]
    if Player1.values.any() == True or Player2.values.any() == True :
        CountP1 =+ len(Player1)
        CountP2 =+ len(Player2)
        print(f"In {x} {P1Name} won {CountP1} times, {P2Name} won {CountP2} times !")
        TotalP1 += len(Player1)
        TotalP2 += len(Player2)
    else :
        print("Check player's spelling! ")
        break
print(f"{P1Name} won {TotalP1} times, while {P2Name} won {TotalP2} times !")


    