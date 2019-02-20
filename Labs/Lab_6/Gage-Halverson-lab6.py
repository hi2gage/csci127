# --------------------------------------
# CSCI 127, Lab 6                      |
# February 21, 2019                    |
# Your Name                            |
# --------------------------------------

#census_file = open("census.txt", "r")
#input_line = census_file.readline()


def average_magnitude(file_name):
    earthquake = open(file_name, "r")
    input_line = earthquake.readline()
    #input_line = earthquake.readline()
    i = 0
    while input_line:
        value = input_line.split(",")
        print(value)
        input_line = earthquake.readline()
        if i > 5:
            break
        i += 1



def earthquake_locations(file_name):
    pass


def count_earthquakes(file_name, lower_bound, upper_bound):
    pass





# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)

    #print("The average earthquake magnitude is {:.2f}\n".format(magnitude))

    #earthquake_locations(file_name)

    #lower_bound = float(input("Enter a lower bound for the magnitude: "))
    #upper_bound = float(input("Enter an upper bound for the magnitude: "))
    #how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    #print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
