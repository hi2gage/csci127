# -----------------------------------------+
# Cole Knudsen                             |
# CSCI 127, Program 2                      |
# Last Updated: Jan 7, 2019                |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+

def flush(hand):
    points = 0
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
        points +=5
    return points

def pair(hand):
    points_pair = 0
    for i in range(len(hand)):
        for n in range(i, len(hand)):
            if hand[i][0] == hand[n][0] and i != n:
                points_pair += 2
    return points_pair

def fifteen(hand):
    dic = {
        "Two" : 2,
        "Three": 3,
        "Four" : 4,
        "Five" : 5,
        "Six" : 6,
        "Seven" : 7,
        "Eight" : 8,
        "Nine" : 9,
        "Ten" : 10,
        "Jack" : 10,
        "Queen" : 10,
        "King" : 10,
        "Ace" : 11
        }
    points_15 = 0
    for i in range(len(hand)):
        for n in range(i, len(hand)):
            if dic[hand[i][0]] == dic[hand[n][0]] and i != n:
                points_15 += 2
    return points_15


def evaluate_hand(hand):
    points_scored = flush(hand) + pair(hand) + fifteen(hand)
    print("Points scored: " + str(points_scored))


def print_hand(hand, number):
    print("Hand " + str(number) + ": " + str(hand))



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
