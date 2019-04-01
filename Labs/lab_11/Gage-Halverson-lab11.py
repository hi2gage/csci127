import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# April 5, 2017
# Your Name
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self, sides):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_high_roll(self):
        roll = self.count_outcomes()
        if roll[7] + roll[8] == 5:
            return True

    def is_it_three_of_a_kind(self):
        roll = self.count_outcomes()
        three = 0
        two = 0
        j = 0
        for i in range(8):
            if roll[i] == 3:
                three = 1
            if roll[i] == 2:
                two = 1
        if two + three == 1 and three == 1:
            return True





    def is_it_large_straight(self):
        pass

# -------------------------------------------------

def main(how_many):

    high_rolls = 0
    three_of_a_kinds = 0
    large_straights = 0
    game = Yahtzee(8)       # 8-sided dice

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_high_roll():
            high_rolls += 1
        elif game.is_it_three_of_a_kind():
            three_of_a_kinds += 1
        elif game.is_it_large_straight():
            large_straights += 1

    #print(game.j)

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of High Rolls:", high_rolls)
    print("Percent:", "{:.2f}%\n".format(high_rolls * 100 / how_many))
    print("Number of Three of a Kinds:", three_of_a_kinds)
    print("Percent:", "{:.2f}%\n".format(three_of_a_kinds * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(50)
