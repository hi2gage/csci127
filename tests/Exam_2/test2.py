# The missing function goes here but write it below. Don’t change any of the provided code.
def count_lines(file_name):
    file = open(file_name, "r")
    i = 0
    for line in file:
        i += 1


    return i

file_name = "question_one.txt"
how_many = count_lines(file_name)
print("There are", how_many, "lines in file", file_name)



"""
A Car runs on gas
A Truck runs on gas
A Bicycle runs on pedal power"""


class Vehicle:
    def __init__(self, type):
        pass
    def __str__(self):
        pass

class

def main():
    car = Vehicle("Car")
    print(car)
    truck = Vehicle("Truck")
    print(truck)
    bicycle = Bicycle()
    print(bicycle)
main()
