# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Gage Halverson                           |
# Last Modified: Feb, 26 2019              |
# -----------------------------------------+
# Provide a brief overview of the program. |
# Provide a brief overview of the program. |
# Provide a brief overview of the program. |
# Provide a brief overview of the program. |
# Provide a brief overview of the program. |
# Provide a brief overview of the program. |
# -----------------------------------------+



def coldest_temperature(input_file):

    #reads file
    temp_file = open(input_file, "r")
    input_line = temp_file.readline()
    input_line = temp_file.readline()#called again to skip reference line

    #creates empty list for all the temp values
    temp_list = []

    #runs through all the lines in the file and adds the temp value to temp_list
    while input_line:
        value_1 = input_line.split(",")
        value_int = int(value_1[-7])

        #Checks to see if temp value is already in temp_list if not, adds it to temp_list
        if temp_list.count(value_int) == 0:
            temp_list.append(value_int)

        #Goes to next line in fle
        input_line = temp_file.readline()

    #creates variable of min temp for later use
    coldest_line = min(temp_list)

    #Goes back to top of the list
    temp_file.seek(0)
    input_line = temp_file.readline()
    input_line = temp_file.readline()#called again to skip reference line

    #Runs through all the lines
    while input_line:
        value_1 = input_line.split(",")
        value_int = int(value_1[-7])

        #finds the right line with the lowest temp
        if value_int == coldest_line:
            value_1 = input_line.split(",")

            #Compiles the City and State
            city = (value_1[5])
            state = (value_1[6])
            location = city +" "+ state
            location = location[1:-1]

            #Complies the Date
            date = value_1[4]
            break

        #Goes to next line in fle
        input_line = temp_file.readline()

    #Prints out values
    print("Coldest Fahrenheit temperature reading:", str(coldest_line))
    print("Location:", str(location))
    print("Date:", str(date))


def average_temperature(input_file, location):
    #reads file
    location_file = open(input_file, "r")
    input_line = location_file.readline()
    input_line = location_file.readline()#called again to skip reference line

    #creates empty list for all the temp values
    temp_list = []

    #runs through all the lines in the file
    num_locations = 0
    while input_line:
        value_1 = input_line.split(",")
        city = (value_1[5])
        state = (value_1[6])
        location_value = city + "," + state
        location_value = location_value[1:-1]

        #adds the temp value to temp_list if location is the same
        if location.lower() == location_value.lower():
            num_locations += 1
            temp_list.append(int(value_1[0]))

        #Goes to next line in fle
        input_line = location_file.readline()

    #prints out number of readings at location
    print("Number of readings: " + str(num_locations))

    #Checks to see if there are temps for locations
    if num_locations == 0:
        print("Average temperature: Not Applicable")
    else:
        average = sum(temp_list)/num_locations
        print("Average temperature: " + "{0:.2f}".format((average)))


def all_stations_by_state(input_file, state):

    #creates list of all the locations
    locations = []

    #Opens file and reads each line into list
    location_file = open(input_file, "r")
    input_line = location_file.readline()
    input_line = location_file.readline()#called again to skip reference line

    #Runs through all the lines
    while input_line:
        value_1 = input_line.split(",")
        state_value = (value_1[-3])
        report_location = value_1[1]

        #checks to see if the states match
        if state.lower() == state_value.lower():

            #checks to see if location is in locations list
            if locations.count(report_location) == 0:
                locations.append(report_location)


        #Goes to next line in fle
        input_line = location_file.readline()

    if len(locations) == 0:
        print("There are no recording stations")
    else:
        #Prints header
        print("Recording Stations \n------------------")

        #prints out the list in format
        for j in range(len(locations)):
            print("{:>2d}".format(j+1) + ".",locations[j])


def largest_spread_of_temp_at_location(input_file, state):

    #creates list of all the spreads
    spread = []

    #Opens file and reads each line into list
    location_file = open(input_file, "r")
    input_line = location_file.readline()
    input_line = location_file.readline()#called again to skip reference line


    #Runs through all the lines
    while input_line:
        value_1 = input_line.split(",")
        state_value = (value_1[-3])
        report_location = value_1[1]

        #checks to see if the states match
        if state.lower() == state_value.lower():
            spread.append(int(value_1[-8]) - int(value_1[-7]))

        #Goes to next line in fle
        input_line = location_file.readline()




    if len(spread) == 0:
        print("There are no recording stations")
    else:
        max_spread = max(spread)
        #Goes back to top of the list
        location_file.seek(0)
        input_line = location_file.readline()
        input_line = location_file.readline()#called again to skip reference line

        #Runs through all the lines
        i = 0
        while input_line:
            state_value = (value_1[-3])
            value_1 = input_line.split(",")
            if state.lower() == state_value.lower():
                if max_spread == (int(value_1[-8]) - int(value_1[-7])):
                    #Compiles the City and State
                    city = (value_1[5])
                    state = (value_1[6])
                    print(state)
                    print(city)
                    location = city +" "+ state
                    location = location[1:-1]

                    #Complies the Date
                    date = value_1[4]
                    print("Widest Spread of Fahrenheit temperature reading:", str(max_spread))
                    print("Location:", str(location))
                    print("Date:", str(date))
                    break

                """else:
                    print("Error accessing file(you most likely entered Washington)")
                    break"""

            #Goes to next line in fle
            input_line = location_file.readline()



# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

def menu():
    print()
    print("1. Identify coldest temperature.")
    print("2. Identify average temperature for a given location.")
    print("3. Identify all recording station locations by state.")
    print("4. Identify Location of Largest Temperature Spread by State.")
    print("5. Quit.")
    print()

# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "weather.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            coldest_temperature(input_file)
        elif (choice == 2):
            location = input("Enter desired location (e.g. Miles City, MT): ")
            average_temperature(input_file, location)
        elif (choice == 3):
            state = input("Enter name of state (e.g. Montana): ")
            all_stations_by_state(input_file, state)
        elif (choice == 4):
            state = input("Enter name of state (e.g. Montana): ")
            largest_spread_of_temp_at_location(input_file, state)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
