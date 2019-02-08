
def legal_play(first_value, first_color, second_value, second_color):
    return [(first_value == second_value) or (first_color == second_color),
            (first_value == second_value), (first_color == second_color)]



list = legal_play(3, "blue", 3, "green")
print("This play works:", str(list[0]), "\nThese values work:", str(list[1]), "\nThese colors work:", str(list[2]))
print("---------------------------")


list = legal_play(4, "yellow", 3, "green")
print("This play works:", str(list[0]), "\nThese values work:", str(list[1]), "\nThese colors work:", str(list[2]))

print("---------------------------")

list = legal_play(3, "blue", 3, "green")

print("This play works:", str(list[0]), "\nThese values work:", str(list[1]), "\nThese colors work:", str(list[2]))
print("---------------------------")
