scores = [0, 31, 27, 31, 49, 21, 17, 25] # [msu-score-1, opponent-score-1, msu-score-2, opponent-score-2, etc.]
# The missing code goes here but write it below. Assume that every game results in either a win or a loss.
wins = 0
losses = 0
for i in range( len(scores)/2):
    if scores[i] > scores[i+1]:
        wins +=1
    else:
        losses +=1
    i +=2


print("MSU has", wins, "win(s) and", losses, "loss(es)")
