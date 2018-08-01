class Building:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.isDestroyed = False

    @property
    def Name(self):
        return self.name

    @property
    def Existed(self):
        return not self.isDestroyed


    def Attacked(self, damage):
        if damage >= self.hp:
            self.hp = 0
            self.isDestroyed = True
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
    def Path(self):
        return self.path



class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    @property
    def Name(self):
        return self.name

    @property
    def GetPlayersOnPath(self, path):
        players = []
        for player in self.members:
            if player.Path == path:
                players.append(player)
        return players


    def AddMember(self, Player):
        self.members.append(Player)
    
    def RemoveMember(self, Player):
        self.members.remove(Player)


class Game:
    def __init__(self, id, team_a, team_b):
        self.id = id
        self.team_a = team_a
        self.team_b = team_b
        self.iteration = 0
        self.gameover = False

    def Start_Game(self):
        while not self.gameover:
            # self.iteration += 1
            # if self.iteration % 100
            pass

    def Fight(self, path):
        member_a = self.team_a.GetPlayersOnPath(path)
        member_b = self.team_b.GetPlayersOnPath(path)
        