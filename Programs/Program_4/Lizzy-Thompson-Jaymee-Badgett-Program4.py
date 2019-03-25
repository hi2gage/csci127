import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Pokedex
# Lizzy Thompson, Jaymee Badgett
# Last Modified: March 15th, 2019
# ---------------------------------------

class Pokemon():
    def __init__(self, name, number, combat_points, types):
        self.name = name
        self.number = number
        self.types = types
        self.combat_points = combat_points

    def __str__(self):
        types = ""
        for i in range(len(self.types)):
            if i > 0:
                types = types + " " + "and " + self.types[i]
            else:
                types += self.types[i]
        return "Number: " + str(self.number) + ", " + "Name: " + self.name + ", " + "CP: " + str(self.combat_points) + ", " + "Type: " + types


    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_types(self):
        return self.types

    def Get_CP(self):
        return self.combat_points


def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")

    #print statement for the pokedex

def print_pokedex(pokedex):
    print()
    print("The Pokedex")
    print("-----------")
    for pokemon in pokedex:
        print(pokemon)


def lookup_by_name(pokedex, name):
    poke_name = []
    exist = 0
    for pokemon in pokedex:
        if pokemon.get_name() == name:
            exist += 1
            print(pokemon)
            print()
    if exist == 0: #checks for names not in the pokedex
        print("No Pokemon named " + name + "\n")

def lookup_by_number(pokedex, number):
    exist = 0
    for pokemon in pokedex:
        if pokemon.get_number() == number:
            exist += 1
            print(pokemon)
            print()
    if exist == 0:
        print ("There is no Pokemon number " + str(number))

def total_by_type(pokedex, pokemon_type):
    poketype_num = 0
    for pokemon in pokedex:
        if pokemon.get_types() == pokemon_type:
            poketype_num += 1
    print("Number of Pokemon that contain type " + pokemon_type + " = " + str(poketype_num))

def average_hit_points(pokedex):
    count = 0
    points_total = 0
    for pokemon in pokedex:
        count += 1
        points_total = points_total + pokemon.Get_CP()
    average = points_total / count
    print("Average Pokemon combat points = " + str(average))

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
