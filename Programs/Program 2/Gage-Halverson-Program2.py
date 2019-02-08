# -----------------------------------------+
# Gage Halverson                           |
# CSCI 127, Program 2                      |
# Last Updated: 2/1/2019                   |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+


#runs through list converting to strings to format the hands for printing
def print_hand(hand_as_list, number):
    print("Hand", number, end=': ')
    i = 0
    while i < 5:
        hand_as_str = ' '.join(hand_as_list[i] )
        print(hand_as_str, end=', ')
        i += 1

# -----------------------------------------+

    print()
#function to convert string face values to int face values
def dic_values(key):
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
    return dic[key]

# -----------------------------------------+

def evaluate_hand(hand_as_list):
    
#if all suits are equal program adds 5 point to score    
    score = 0
    if hand_as_list[0][1] == hand_as_list[1][1] == hand_as_list[2][1] == hand_as_list[3][1] == hand_as_list[4][1]:
        score += 5
    
#Runs through all the possible combinations to see if the face values equal each other
    j = 0 
    while j < 5:
        k = j+1
        while k < 5:
            value_1 = dic_values(hand_as_list[j][0])
            value_2 = dic_values(hand_as_list[k][0])
            if  value_1 == value_2:
                score += 2
            k += 1
        j +=1
#Runs through all the possible combinations to see if the face values added together equal 15

    j = 0 
    while j < 5:
        k = j+1
        while k < 5:
            value_1 = dic_values(hand_as_list[j][0])
            value_2 = dic_values(hand_as_list[k][0])
            if  value_1 + value_2 == 15:
                score += 2
            k += 1
        j +=1

    print("Points Scored:", score)
    print()


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
    cribbage_file = open("cribbage.txt", "r")
    process_hands(cribbage_file, 5)
    cribbage_file.close()

# -----------------------------------------+

main()
