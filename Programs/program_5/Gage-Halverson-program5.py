import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Peg Rectangle Solitaire    |
# Your Name(, Your Partner's Name)      |
# Last Modified: ??, 2019               |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# ---------------------------------------
# Start of PegRectangleSolitaire Class  |
# ---------------------------------------

class PegRectangleSolitaire:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1

# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " * |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer

# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|
    def legal_move(self, row_start, col_start, row_end, col_end):
        #first checks to see if
        two_away = False
        if self.board[row_start][col_start] == True:
            if abs(row_start - row_end) == 2 and abs(col_start - col_end) == 0:
                two_away = True
            elif abs(row_start - row_end) == 2 and abs(col_start - col_end) == 2:
                two_away = True
            elif abs(row_start - row_end) == 0 and abs(col_start - col_end) == 2:
                two_away = True
            else:
                return False
        else:
            return False

        if two_away == True:
            if row_start > row_end:
                remove_row = row_end + 1
            elif row_start == row_end:
                remove_row = row_end
            elif row_start < row_end:
                remove_row = row_end - 1
            else:
                remove_row = row_end - 1


            if col_start > col_end:
                remove_col = col_end + 1
            elif col_start == col_end:
                remove_col = col_start
            else:
                remove_col = col_end - 1
            if self.board[remove_row][remove_col] == True:
                return True
            else:
                return



    def make_move(self, row_start, col_start, row_end, col_end):
        self.pegs_left += -1
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True


        if row_start > row_end:
            remove_row = row_end + 1
        elif row_start == row_end:
            remove_row = row_end
        elif row_start < row_end:
            remove_row = row_end - 1
        else:
            remove_row = row_end - 1


        if col_start > col_end:
            remove_col = col_end + 1
        elif col_start == col_end:
            remove_col = col_start
        else:
            remove_col = col_end - 1

        self.board[remove_row][remove_col] = False



    def game_won(self):
        if self.pegs_left == 1:
            return True

    def final_message(self):
        print("Number of pegs left: " + str(self.pegs_left))
        if self.pegs_left == 1:
            print("You're a genius!")
        elif self.pegs_left == 2:
            print("You're pretty smart.")
        elif self.pegs_left == 3:
            print("You're just average.")
        else:
            print("You're just plain dumb.")

# ---------------------------------------
# End of PegRectangleSolitaire Class    |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Peg Rectangle Solitaire!")
    print("-----------------------------------\n")

    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1
    game = PegRectangleSolitaire(rows, columns, row, column)
    print()

    keep_going = "yes"
    print(game)
    print(game.game_won())
    while (not game.game_won() and keep_going.lower() == "yes"):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is now allowed.")
        print()
        print(game)
        if not game.game_won():
            keep_going = input("Do you want to continue (yes or no): ")

    game.final_message()

# ---------------------------------------

main()
