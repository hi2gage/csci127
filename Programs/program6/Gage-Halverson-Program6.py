import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive




def main(file_name):
    csv_data = pd.read_csv(file_name)

    #|Pie Chart of 5 different types of delays and how offen they occur
    #The Pie Chart shows that a majority of delays come
    #from the National Aviation System, and that very
    #few delays come from weather. After doing more research,
    #NAS delays may include: non-extreme weather conditions,
    #airport operations, heavy traffic volume, air traffic control, etc.
    #This shows that NAS has a lot control over when planes take off and
    #land which is great!

    #Creates data_frame from csv_file only using certain columns
    data_frame_pie = pd.DataFrame(data = csv_data, columns=['# of Delays.Carrier',\
                                                        '# of Delays.Late Aircraft',\
                                                        '# of Delays.National Aviation System',\
                                                        '# of Delays.Security','# of Delays.Weather']).sum()


    #Plots a pie graph
    data_frame_pie.plot(kind='pie', autopct='%1.1f%%', legend=False, title='Distribution of Types of Delay', pctdistance=1.2, \
                        labeldistance=1.35, labels=['of Delays from Carrier',\
                            'Delays from Late Aircraft',\
                            'of Delays from National Aviation System',\
                            'of Delays from Security','of Delays from Weather'])

    #creates a white hole in the middle
    centre_circle = plt.Circle((0,0),0.5,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    interactive(True)


    #Second plot show correlation between delayed and cancelled flights per year. This shows
    #that when there are delayed flights, whatever is causing the delay might also be causing
    #flights to be cancelled. Cancellations have more random fluctuations then delayed flights.

    #Creates data_frame from csv_file only only with Cancelled and Delayed columns
    data_frame_line = pd.DataFrame(data = csv_data, columns=['Cancelled','Delayed', 'Year'])

    #groups the data by year and sums column by year
    df = data_frame_line.groupby('Year')['Delayed','Cancelled'].sum()

    #creates axis with Delayed Flights scaled Y-axis on right and Cancelled Flights scaled on left
    ax = df.plot(secondary_y='Delayed', title="Cancelled and Delayed Flights per year")
    ax.set_ylabel('# of Cancelled Flights')
    ax.right_ax.set_ylabel('# of Delayed Flights')

    #shows plot
    plt.show()




main("airlines.csv")
