# --------------------------------------
# CSCI 127, Lab 6                      |
# February 21, 2019                    |
# Gage Halverson                       |
# --------------------------------------


def average_magnitude(file_name):
    #Opens file and reads each line into list
    earthquake = open(file_name, "r")
    input_line = earthquake.readline()
    input_line = earthquake.readline() #called again to skip reference line

    #creates vars to keep track of sum and how many variables
    number_values = 0
    sum_value = float(0)

    #runs through all the magnitudes of all the earthquakes
    while input_line:
        value = input_line.split(",")
        sum_value += float(value[-8])
        number_values += 1
        input_line = earthquake.readline()

    return (sum_value/number_values)



def earthquake_locations(file_name):
    #prints header
    print("Alphabetical Order of Earthquake Locations \n------------------------------------------")

    #Opens file and reads each line into list
    earthquake = open(file_name, "r")
    input_line = earthquake.readline()
    input_line = earthquake.readline()#called again to skip reference line

    #creates list of all the locations
    locations = []

    #runs through all the locations
    while input_line:
        value_1 = input_line.split(",")

        #makes sure that location isn't already in the list
        if locations.count(value_1[-5]) == 0:
            locations.append(value_1[-5])
        input_line = earthquake.readline()

    locations.sort()

    #prints out the list in format
    for j in range(len(locations)):
        print("{:>3d}".format(j) + ".",locations[j])
    print()


def count_earthquakes(file_name, lower_bound, upper_bound):
    #Opens file and reads each line into list
    earthquake = open(file_name, "r")
    input_line = earthquake.readline()
    input_line = earthquake.readline() #called again to skip reference line

    #creates for all the locations
    locations = []
    while input_line:
        values = input_line.split(",")
        locations.append(float(values[-8]))
        input_line = earthquake.readline()

    i = 0
    count = 0
    for _ in locations:
        if float(locations[i]) >= float(lower_bound) and float(locations[i]) <= float(upper_bound):
            count += 1
        i += 1

    return count

# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)

    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))

    earthquake_locations(file_name)

    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
