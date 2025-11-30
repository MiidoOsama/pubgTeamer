import random

team = []
def add_players():
    players = list(input('Enter Players name :').split(','))
    return players

def random_choice(players):
    if len(players) == 8 or len(players) == 7:
        team = random.sample(players, k=4)


    elif len(players) == 6 or len(players) == 5:
        team = random.sample(players, k=3)

    elif len(players) == 4 :
        team = random.sample(players, k=2)


    else : 
        print("Error!")

    return team

def main():
    PUBG_TEAMER = """
WELCOME TO PUBG TEAMER

Enter player names in lobby
"""

players = add_players()
team = random_choice(players)

print(f"Team: {team}")


main()