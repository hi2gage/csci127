import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# April 11, 2017                                  |
# Gage Halverson                                  |
# -------------------------------------------------

def read_file(file_name):
    with open(file_name) as file:
        #creates empty lists for data
        college_names_list = []
        college_enrollments_list = []

        #skips first line of file
        file.readline()
        #loops through file appending each item to different lists
        for line in file:
            line = line.split(",")
            college_names_list.append(line[0])
            college_enrollments_list.append(int(line[1]))

    #creates numpyarrays using lists
    college_names = np.array(college_names_list)
    college_enrollments = np.array(college_enrollments_list)

    #passes arrays
    return college_names, college_enrollments


# -------------------------------------------------

def main(file_name):
    #numpy arrays with data
    college_names, college_enrollments = read_file(file_name)

    #sets top limit to 4400
    plt.ylim(top=4400)

    #sets yticks to np array
    plt.yticks(np.arange(0,4401,400))

    #creates labels for graph and window
    plt.xlabel('College Name')
    plt.ylabel('College Enrollment')
    fig = plt.figure(1)
    fig.canvas.set_window_title('Montana State University Fall 2018 Enrollments')
    #plt.figure('Montana State University Fall 2018 Enrollments')


    #plots data on bar graph
    plt.bar(college_names, college_enrollments, color=["blue", "gold"])

    plt.show()
# -------------------------------------------------

main("fall-2018.csv")
