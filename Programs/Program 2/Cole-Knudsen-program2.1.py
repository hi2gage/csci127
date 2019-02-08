# -----------------------------------------+
# Cole Knudsen                             |
# CSCI 127, Program 2                      |
# Last Updated: Jan 7, 2019                |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+

def flush(hand):
        return 5

def pair(hand):
    return 2

def fifteen(hand):
    return 2
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
