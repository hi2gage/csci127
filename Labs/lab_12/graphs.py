# --------------------------------------
# CSCI 127: Joy and Beauty of Data
# MatPlotLib Introductory Example
# --------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math

# --------------------------------------

def plot_line(x1, y1, x2, y2):
    """Plot a line using the specified points."""
    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x, y, linestyle='--', color='magenta')


# --------------------------------------

def plot_sine_wave(start_x, stop_x, amplitude):
    """Plot a sine wave."""
    x_array = np.linspace(start_x, stop_x, 1000)
    y_array = amplitude * np.sin(x_array)
    print(x_array)
    plt.plot(x_array, y_array, linewidth='5')

# --------------------------------------

def main(graph_min, graph_max):
    plt.axis([graph_min, graph_max, graph_min, graph_max])
    #plt.xlim(graph_min, graph_max)
    #plt.ylim(graph_min, graph_max)
    plt.xlabel("x")
    plt.ylabel("y")

    plot_line(graph_min, graph_min, graph_max, graph_max)

    x_array = np.array([graph_min, graph_max])
    y_array = np.array([graph_max, graph_min])
    print(x_array)
    print(y_array)
    plt.plot(x_array, y_array, linestyle='--', color='magenta')

    plot_sine_wave(graph_min, graph_max, graph_max // 4)

    plt.show()

# --------------------------------------

main(-200, 200)
