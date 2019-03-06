#Create a class named Pokemon that has the following instance
#variables: number, name and combat_points.
#Add a constructor method that enables a new Pokémon to be created.
#Add methods named get_name, get_number, get_combat_points and set_combat_points.
#Write a program that utilizes the functionality of the Pokémon class in its entirety.


class Pokemon:
    def __init__(self, number, name, combat_points):
        self.number = number
        self.name = name
        self.combat_points = combat_points

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_combat_points(self):
        return self.combat_points

    def set_combat_points(self, combat_points):
        self.combat_points = combat_points

    def print_entry(self):
        print("{} -- {} -- {}".format(str(self.number), str(self.name), str(self.combat_points)))



def print_pokemon(contacts):
    print("My Pokemon")
    print("-----------")
    for person in contacts:
        person.print_entry()
    print("-----------\n")


def main():
    pokemon_1 = Pokemon(1,"bulbasaur",318)
    pokemon_2 = Pokemon(2,"Ivysaur",405)
    pokemon_3 = Pokemon(3, "Venusaur", 525)

    pokemon_total = [pokemon_1, pokemon_2, pokemon_3]
    print_pokemon(pokemon_total)

    what_pokemon = input("Which Pokemon combat points do you want to edit? ")
    new_combat_points = input("How many combat points? ")

    for pokemon in pokemon_total:
        print(pokemon.name)
        if pokemon.name == what_pokemon:
            pokemon.set_combat_points(new_combat_points)
            break

    print("-----------New Pokemon Scores-------")
    pokemon_total = [pokemon_1, pokemon_2, pokemon_3]
    print_pokemon(pokemon_total)

main()
