"""Create a class named Pokemon that has the following instance
variables: number, name and combat_points.
Add a constructor method that enables a new Pokémon to be created.
Add methods named get_name, get_number, get_combat_points and set_combat_points.
Write a program that utilizes the functionality of the Pokémon class in its entirety.
"""

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


def main():
    pokemon_1 = Pokemon(1,"bulbasaur",318)
    name = pokemon_1.get_number()
    print(name)



main()
