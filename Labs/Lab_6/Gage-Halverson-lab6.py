# --------------------------------------
# CSCI 127, Lab 6                      |
# February 21, 2019                    |
# Gage Halverson                       |
# --------------------------------------

#census_file = open("census.txt", "r")
#input_line = census_file.readline()


def average_magnitude(file_name):
    earthquake = open(file_name, "r")
    input_line = earthquake.readline()
    #input_line = earthquake.readline()
    i = 0
    sum_value = float(0)
    input_line = earthquake.readline()
    while input_line:
        value = input_line.split(",")
        sum_value += float(value[-8])
        i += 1
        input_line = earthquake.readline()
    return (sum_value/i)



def earthquake_locations(file_name):
    print("Alphabetical Order of Earthquake Locations \n------------------------------------------")
    earthquake = open(file_name, "r")
    input_line = earthquake.readline()
    input_line = earthquake.readline()
    locations = []
    while input_line:
        value_1 = input_line.split(",")
        if locations.count(value_1[-5]) == 0:
            locations.append(value_1[-5])
        input_line = earthquake.readline()

    locations.sort()
    for j in range(len(locations)):
        print("  "+ str(j) +". " +locations[j])


def count_earthquakes(file_name, lower_bound, upper_bound):
    print(lower_bound)
    print(upper_bound)


# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)

    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))

    earthquake_locations(file_name)

    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    #print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
