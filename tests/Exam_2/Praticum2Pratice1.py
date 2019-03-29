###--------------------------------------------------------###
###---------------------Question 1-------------------------###
###--------------------------------------------------------###
"""
def count_lines(file_name):
    file=open(file_name, "r")
    lines=0
    for line in file:
        lines+=1
    return lines
    file.close()


file_name = "cribbage.txt"
how_many = count_lines(file_name)
print("There are", how_many, "lines in file", file_name)

print()

###--------------------------------------------------------###
###----------------Question 2------------------------------###
###--------------------------------------------------------###

class Vehicle:
    def __init__(self, kind):
        self.kind = kind

    def get_Kind(self):
        return(self.kind)

    def __str__(self):
        return "A "+ self.kind +" runs on gas"

class Bicycle:
    def __str__(self):
        return "A Bicycle runs on pedal power"


def main():
    car = Vehicle("Car")
    print(car)
    truck = Vehicle("Truck")
    print(truck)
    bicycle = Bicycle()
    print(bicycle)
main()

print()
"""
###--------------------------------------------------------###
###----------------Question In Class-----------------------###
###--------------------------------------------------------###

class Vehicle:
    def __init__(self, kind):
        self.kind = kind
        self.fuel="gas"

    def __str__(self):
        return "A "+ self.kind +" runs on "+ self.fuel

class Bicycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Bicycle")
        self.fuel="pedal power"


def main():
    car = Vehicle("Car")
    print(car)
    truck = Vehicle("Truck")
    print(truck)
    bicycle = Bicycle()
    print(bicycle)

main()
