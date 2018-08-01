from pydota import Player, Team, Building, Game

def main():
    T1 = Team("Balala")
    T2 = Team("BotTeam")

    T1_players = [
        Player("Chacha", 90, "TOP"),
        Player("Unknown", 90, "TOP"),
        Player("Sstylle",90, "MID"),
        Player("Jordan", 90, "BTM"),
        Player("Unknown", 90, "BTM"),
    ]
    T2_players = [
        Player("Bot1", 85, "TOP"),
        Player("Bot2", 80, "TOP"),
        Player("Bot3", 75, "MID"),
        Player("Bot4", 95, "BTM"),
        Player("Bot5", 85, "BTM"),
    ]
 
    for p1, p2 in zip(T1_players, T2_players):
        T1.AddMember(p1)
        T2.AddMember(p2)

    game = Game(1, T1, T2)
    game.Start_Game()

    return 0
    

if __name__ == '__main__':
    main()
