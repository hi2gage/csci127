class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)\


class Game:
    def __init__(self, team_1, score_1, team_2, score_2, Date):
        self.team_1 = team_1
        self.score_1 = score_1
        self.team_2 = team_2
        self.score_2 = score_2
        self.Date = Date
    def __str__(self):
        if self.score_1 > self.score_2:
            output = str(self.team_1) + " beat " + \
             str(self.team_2) + " on " + str(self.Date) \
             + ": " + str(self.score_1) + " to " + \
             str(self.score_2)

        if self.score_1 < self.score_2:
            output = str(self.team_2) + " beat " + \
             str(self.team_1) + " on " + str(self.Date) \
             + ": " + str(self.score_2) + " to " + \
             str(self.score_1)
             
        return output

# -----------------------------------------------------------

championship = Game("Montana State", 62, "Idaho State", 56, Date(3, 11, 2017))
print(championship)

ncaa = Game("Montana State", 63, "Washington", 91, Date(3, 18, 2018))
print(ncaa)
