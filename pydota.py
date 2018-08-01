from game import Battle, PathToHappen

class Building:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.isDestroyed = False

    @property
    def Name(self):
        return self.name

    @property
    def HP(self):
        return self.hp

    def TakeDamage(self, damage):
        # damage = abs(int(damage))
        if damage >= self.hp:
            self.hp = 0
            self.isDestroyed = True
            print("BOOM! {0} has been destroyed!".format(self.name))
        else:
            self.hp -= damage

        

class Player:
    def __init__(self, name, score, path):
        self.name = name
        self.score = score
        self.path = path
    
    @property
    def Name(self):
        return self.name

    @property
    def Score(self):
        return self.score

    @property
    def Path(self):
        return self.path



class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    @property
    def Name(self):
        return self.name

    def GetPlayersOnPath(self, path):
        players = []
        for player in self.members:
            if player.Path == path:
                players.append(player)
        return players

    def GetScoreOnPath(self, path):
        score_multiplyer = (0, 1, 0.8, 0.65, 0.55, 0.5)
        scores = [x.Score for x in self.GetPlayersOnPath(path)]
        return sum(scores) * score_multiplyer[len(scores)]

    def AddMember(self, Player):
        self.members.append(Player)
    
    # to-do: remove by name
    # def RemoveMember(self, Player):
    #     self.members.remove(Player)


class Game:
    def __init__(self, id, team_a, team_b):
        self.id = id
        self.team_a = team_a
        self.team_b = team_b
        self.iteration = 0
        self.gameover = False
        self.Init_Map()


    def Init_Map(self):
        building_dict = {
            "BASE": {'Hp': 500},
            "TOWER_1": {'Hp': 300},
            "TOWER_2": {'Hp': 200},
            "TOWER_3": {'Hp': 100},
        }
        self.map_info = {}
        for team in ["A", "B"]:
            for key in building_dict:
                if key == "BASE":
                    name = '_'.join([team, key])
                    self.map_info[name] = Building(name, building_dict[key]['Hp'])
                else:
                    for path in ["TOP", "MID", "BTM"]:
                        name = '_'.join([team, path, key])
                        self.map_info[name] = Building(name, building_dict[key]['Hp'])

    def Start_Game(self):
        # while not self.gameover:
        #     self.iteration += 1
        self.PrintTeamInfo()
        print("Game began!")
        while not self.IsGameOver():
            choice = PathToHappen()
            self.Fight(choice)

    def Fight(self, path):
        power_a = self.team_a.GetScoreOnPath(path)
        power_b = self.team_b.GetScoreOnPath(path)
        result = Battle(power_a, power_b)
        if result > 0: 
            loser = 'B'
        else:
            loser = 'A'
        building = self.GetBuildingToDamage(loser, path)
        if building:
            damage = abs(int(result))
            building.TakeDamage(damage)
            print("{0} takes damage: {1}, current HP: {2}".format(building.Name, damage, building.HP))

    def GetBuildingToDamage(self, team, path):
        if not self.map_info["_".join([team, path, "TOWER_3"])].isDestroyed:
            return self.map_info["_".join([team, path, "TOWER_3"])]
        elif not self.map_info["_".join([team, path, "TOWER_2"])].isDestroyed:
            return self.map_info["_".join([team, path, "TOWER_2"])]
        elif not self.map_info["_".join([team, path, "TOWER_1"])].isDestroyed:
            return self.map_info["_".join([team, path, "TOWER_1"])]
        elif not self.map_info["_".join([team, "BASE"])].isDestroyed:
            return self.map_info["_".join([team, "BASE"])]
        else:
            return None

    def IsGameOver(self):
        if self.map_info["A_BASE"].isDestroyed:
            print("Team A Lose!")
            return True
        if self.map_info["B_BASE"].isDestroyed:
            print("Team B Lose!")
            return True
        else:
            return False

    def PrintTeamInfo(self):
        print("Team A: {0}".format(self.team_a.Name))
        print("\tPlayer:")
        for player in self.team_a.members:
            print("\t\tName: {0}\tScore: {1}\tPath:{2}".format(player.Name, player.Score, player.Path))
        print('-'*20)
        print("Team B: {0}".format(self.team_b.Name))
        print("\tPlayer:")
        for player in self.team_b.members:
            print("\t\tName: {0}\tScore: {1}\tPath:{2}".format(player.Name, player.Score, player.Path))