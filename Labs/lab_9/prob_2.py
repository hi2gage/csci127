class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    def __init__(self, manufacturer, refrigerant):
        self.refrigerant = refrigerant
    def __str__(self):
        return self.refrigerant

# The missing code goes here but write it below.
my_refrigerator = Refrigerator("Samsung", "R134a")
print(my_refrigerator)
