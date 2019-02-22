# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Weather CSV Library           |
# Your Name(, Your Partner's Name)         |
# Last Modified: ??, 2019                  |
# -----------------------------------------+
# Provide a brief overview of the program. |
# -----------------------------------------+



def coldest_temperature(input_file):

    temp_file = open(input_file, "r")
    input_line = temp_file.readline()
    input_line = temp_file.readline()#called again to skip reference line

    #creates list of all the locations
    temp_list = []

    #runs through all the locations
    while input_line:
        value_1 = input_line.split(",")

        #makes sure that location isn't already in the list
        value_int = int(value_1[-7])
        if temp_list.count(value_int) == 0:
            temp_list.append(value_int)
        input_line = temp_file.readline()

    temp_list.sort()
    print(min(temp_list))


    coldest = 5
    location = "Bettles AK"
    date = "12/4/2016"
    print("Coldest Fahrenheit temperature reading:", str(coldest))
    print("Location:", str(location))
    print("Date:", str(date))


def average_temperature(input_file, location):
    pass

def all_stations_by_state(input_file, state):
    pass





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
    print("4. Something interesting, non-trivial and not a variation of the above options.")
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
            pass
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
