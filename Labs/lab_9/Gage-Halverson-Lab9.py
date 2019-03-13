# Problem 1

score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

# The missing code goes here but write it below. Assume that every game results in either a win or a loss.
wins = 0
losses = 0
dic_list = list(score_differences.values())
for num in dic_list:
    if num > 0:
        wins +=1
    else:
        losses +=1

# End of Code added

print(wins, "wins -", losses, "losses")


# Problem 2

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
print(str(my_refrigerator))
# R134a is the refrigerant (cooling agent) used
