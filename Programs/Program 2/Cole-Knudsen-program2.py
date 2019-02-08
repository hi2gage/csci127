# -----------------------------------------+
# Cole Knudsen                             |
# CSCI 127, Program 2                      |
# Last Updated: Jan 7, 2019                |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+
def flush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        return 5

def pair(hand):
    points = 0
    for i in len(hand):
        for n in range(i, len(hand)):
            if hand[i][0] == hand[n][0] and i != n:
                points += 2
    return points

def fifteen(hand):
    pass
def evaluate_hand(hand):
    points_scored = flush(hand) + pair(hand) + fifteen(hand)


def print_hand(hand, number):
    print("Hand " + number + ": " + hand)
    print("Points scored: " + points_scored)


# -----------------------------------------+
# Do not change anything below this line.  |
# -----------------------------------------+

def process_hands(cribbage_input, cards_in_hand):
    number = 1
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0].capitalize(), hand[1].capitalize()])
            hand = hand[2:]
        print_hand(hand_as_list, number)
        evaluate_hand(hand_as_list)
        number += 1

# -----------------------------------------+

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 5)
    cribbage_file.close()

# -----------------------------------------+

main()
