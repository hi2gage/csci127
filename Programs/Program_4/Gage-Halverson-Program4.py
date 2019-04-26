import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# Gage Halverson                        |
# Last Modified: March, 6th 2019        |
# ---------------------------------------
# This program uses objects to create
# different Pokemon then compile them
# into a list of all the Pokemon. The
# program can then prompts the user to
# decide what they want to use too lookup
# data about that Pokemon.
# ---------------------------------------
class Pokemon:
    #creates class objects
    def __init__(self, name, number, combat_points, types):
        self.number = number
        self.name = name
        self.combat_points = combat_points
        self.types = types

    #Special String method explaining how to print objects
    def __str___(self):
        pokemon_print = "Number: " + str(self.number) \
        + ", Name: " + str(self.name).capitalize() \
        + ", CP: " + str(self.combat_points) \
        + ": Type: " + str(', '.join(self.types).replace(",", " and"))
        return pokemon_print

    #looks up name of object
    def Get_name(self):
        return self.name

    #looks up number of object
    def Get_number(self):
        return self.number

    #looks up name of object
    def Get_type(self):
        return list(self.types)

    #looks up Combat Points of object
    def Get_CP(self):
        return self.combat_points

#Finds pokemon in list of objects by name
#then uses string to print the object
def lookup_by_name(pokedex, name):
    exists = False
    for pokemon in pokedex:
        if pokemon.Get_name() == name:
            print(pokedex)
            exists = True
            break
    if exists == False:
        print("There is no Pokemon named " + name)

#Finds pokemon in list of objects by number
#then uses string to print the object
def lookup_by_number(pokedex, number):
    exists = False
    for pokemon in pokedex:
        if pokemon.Get_number() == number:
            print(pokedex)
            exists = True
            break
    if exists == False:
        print("There is no Pokemon number " + str(number))

#Goes through all the objects in list and counts how many of certain type
def total_by_type(pokedex, pokemon_type):
    count_type = 0
    for pokemon in pokedex:
        count_type += pokemon.Get_type().count(pokemon_type.lower())
    print("Number of Pokemon that contain type " \
        + pokemon_type.capitalize() \
        + " = " + str(count_type))

#Adds all the Combat Points of all objects in list then finds average
def average_hit_points(pokedex):
    i = 0
    points_count = 0
    for pokemon in pokedex:
        points_count += int(pokemon.Get_CP())
        i += 1
    average = points_count/i
    print("Average Pokemon combat points = " + str(round(average, 2)))


#Goes through list of objects and prints all of them
def print_pokedex(pokedex):
    print()
    print("The Pokedex")
    print("-----------")
    i = 0
    for pokemon in pokedex:
        print(pokedex, sep = "\n")
        i += 1

#Prints out menu options
def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon with Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit")
    print()

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
