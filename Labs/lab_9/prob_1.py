#Question One. 50 points. Supply the missing Python code below.
#The scores_differences dictionary contains the difference between
#Montana State’s football score and its opponent’s football score on
#a given date. For example, on October 21, 2017, Montana State scored
#27 points and Northern Colorado scored 24 points, so the difference
#is 3. In the example below, the output 2 wins – 1 losses should be printed.
#The solution should be of high quality and work correctly regardless of how
#many entries are in the dictionary. Comments are not necessary.


score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3
score_differences["October 25, 2017"] = -12
score_differences["October 21, 2018"] = 4

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
