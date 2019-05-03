def calculate_calories(my_order, nutrition_info):
    calories = 0
    for items in my_order:
        for info in nutrition_info:
            if info[0] == items[0]:
                calories += info[1]*items[1]

    return calories


# The missing function goes here but write it below.
# Each sublist contains the name of a McDonald’s item, followed by the calories in that item
nutrition_info = [["denali big mac", 850], ["artisan grilled chicken", 440], ["medium fries", 340],
                ["large coke", 290], ["chocolate chip cookie", 170]]
# The following order consists of 2 denali big macs, 1 medium fries and 1 large coke
my_order = [["denali big mac", 2], ["medium fries", 1], ["large coke", 1]]
# For this example, the correct output is Calories in order = 2330
print("Calories in order =", calculate_calories(my_order, nutrition_info))
