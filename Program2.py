# --------------------------------------
# CSCI 127, Lab 4
# February 7, 2019
# Gage Halverson
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")

# --------------------------------------

def process_seasons(seasons):
    i = 1
    while i <= len(seasons):
        process_season(i, seasons[i-1][0], seasons[i-1][1])

        #converting lists for that season into varibles
        games_played = seasons[i-1][0]
        season_points = seasons[i-1][1]
        #creating and reseting varibles
        wins = 0
        ties = 0
        loses =  0
        j = 0
        #sets the first max amount of wins
        wins = int((season_points / 3))

        #loops through checking for different combinations with 1 less win each time
        while (wins + loses + ties) <= season_points:
            ties = j*3
            ties += season_points % 3
            loses = games_played - wins - ties
            if (abs(wins) + abs(ties) + abs(loses) > games_played):
                break

            #prints out wins, ties and loses
            print(str(wins)+"-"+str(ties)+"-"+str(loses))

            wins -=1
            j += 1
        print("")
        i += 1

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]

    process_seasons(soccer_seasons)

# --------------------------------------

main()
