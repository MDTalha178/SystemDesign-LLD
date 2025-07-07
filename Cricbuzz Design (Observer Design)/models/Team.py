from models.player import Player


class Team:
    team_id: str
    total_player: int
    team_name: str
    player: list[Player] = []

    def __init__(self, team_id, total_player, team_name, player):
        self.team_id = team_id
        self.total_player = total_player
        self.team_name = team_name
        self.player = player

    def get_team_id(self):
        return self.team_id

    def get_total_player(self):
        return self.total_player

    def get_team_name(self):
        return self.team_name

    def get_player(self):
        return self.player