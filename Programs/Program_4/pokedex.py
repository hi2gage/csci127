import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Your Name(, Your Partner's Name)      |
# Last Modified: ??, 2019               |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------
class Pokemon:
    def __init__(self, name, number, combat_points, types):
        self.number = number
        self.name = name
        self.combat_points = combat_points
        self.types = types

    def __str___(self):
        pokemon_print = "Number: " + str(self.number) \
        + ", Name: " + str(self.name) \
        + ", CP: " + str(self.combat_points) \
        + ": Type: " + str(', '.join(self.types).replace(",", " and"))
        return pokemon_print

    def Lookup_by_name(self):
        return self.name





def lookup_by_name(pokedex, name):
    i = 0
    print(name)
    print(pokedex[i].Lookup_by_name())

def lookup_by_number(pokedex, number):
    pass

def total_by_type(pokedex, pokemon_type):
    pass

def average_hit_points(pokedex):
    pass


def print_pokedex(pokedex):
    print()
    print("The Pokedex")
    print("-----------")
    i = 0
    for pokemon in pokedex:
        print(pokedex[i].__str___(), sep = "\n")
        i += 1

        #print(pokedex[0].__str___())

def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")



# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
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
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
