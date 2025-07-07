from datetime import datetime

from models.Innings import Innings
from models.Team import Team


class Match:
    match_id: str
    match_date: datetime
    match_venue: str
    commentary: list
    team1: Team
    team2: Team
    innings1: Innings
    innings2: Innings
    is_first_innings: bool

    def __init__(self, match_id, match_date, match_venue, commentary, team1, team2, innings1, innings2):
        self.match_id = match_id
        self.match_date = match_date
        self.match_venue = match_venue
        self.commentary = commentary
        self.team1 = team1
        self.team2 = team2
        self.innings1 = innings1
        self.innings2 = innings2
        self.is_first_innings = True

    def get_is_first_innings(self) -> bool:
        return self.is_first_innings

    def get_match_id(self):
        return self.match_id

    def get_match_date(self):
        return self.match_date

    def get_match_venue(self):
        return self.match_venue

    def get_commentary(self):
        return self.commentary

    def get_team1(self):
        return self.team1

    def get_team2(self):
        return self.team2

    def get_innings1(self):
        return self.innings1

    def get_innings2(self):
        return self.innings2