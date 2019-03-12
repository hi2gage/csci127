class Appliance():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    def __init__(self, manufacturer, refrigerant):
        Appliance.__init__(self, manufacturer)
        self.refrigerant = refrigerant
    def __str__(self):
        print_str = self.refrigerant + " is the refrigerant (cooling agent) used"
        return print_str

# The missing code goes here but write it below.
my_refrigerator = Refrigerator("Samsung", "R134a")
print(my_refrigerator)
# R134a is the refrigerant (cooling agent) used

#print(help(Refrigerator))
