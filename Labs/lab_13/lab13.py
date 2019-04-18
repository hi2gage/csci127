import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

# -------------------------------------------------
# CSCI 127, Lab 13                                |
# April 18, 2019                                  |
# Your Name                                       |
# -------------------------------------------------

def main(file_name):
    info = pd.read_csv(file_name)
    welp = pd.DataFrame(data=info)
    #print(welp)
    #print()


    x_axis = welp.columns.values[0]
    y_axis = welp.columns.values[1]
    #print(x_axis)
    #print(y_axis)


    welp.plot(x=str(x_axis), y=str(y_axis), kind="bar", color=["blue", "gold"], legend = None, title = file_name[:-4])
    #data.plot.bar(x=str(x_axis), y=str(y_axis), color=["blue", "gold"], legend = None)

    plt.xlabel(x_axis)      # Note: x-axis should be determined above
    plt.ylabel(y_axis)      # Note: y-axis should be determined above
    #interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

main("MSU College Enrollments.csv")
main("CS Faculty.csv")
