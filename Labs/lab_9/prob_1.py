score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

# The missing code goes here but write it below. Assume that every game results in either a win or a loss.

wins = 0
losses = 0
dic_list = list(score_differences.values())
for num in dic_list:
    if num > 0:
        wins +=1
    else:
        losses +=1
print(wins, "wins -", losses, "losses")
