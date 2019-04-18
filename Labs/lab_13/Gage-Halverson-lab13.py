import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# April 18, 2019                                  |
# Gage Halverson                                  |
# -------------------------------------------------

def main(file_name):
    # read the file_name into a pandas dataframe
    data = pd.read_csv(file_name)

    column_names= list(data.columns.values)
    x_axis = str(column_names[0])
    y_axis = str(column_names[1])
    #plt.figure(0)
    data.plot(x=x_axis, y=y_axis, kind="bar", color=["blue", "gold"], legend = None, title = file_name[:-4])
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"

    # The only four statements that may use the matplotlib library appear next.
    # Do not modify them.
    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
