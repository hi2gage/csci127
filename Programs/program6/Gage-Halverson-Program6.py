import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive




def main(file_name):
    csv_data = pd.read_csv(file_name)

    #Pie Chart of types of delays
    #The Pie Chart shows that a majority of delays come
    #from a
    data_frame_pie = pd.DataFrame(data = csv_data, columns=['# of Delays.Carrier',\
                                                        '# of Delays.Late Aircraft',\
                                                        '# of Delays.National Aviation System',\
                                                        '# of Delays.Security','# of Delays.Weather']).sum()
    print(data_frame_pie)
    explode = (10,10,10,10)
    data_frame_pie.plot(kind='pie', autopct='%1.1f%%', legend=False, title='Distribution of Types of Delay', pctdistance=1.2, \
                        labeldistance=1.35, labels=['of Delays from Carrier',\
                            'of Delays from Late Aircraft',\
                            'of Delays from National Aviation System',\
                            'of Delays from Security','of Delays from Weather'])

    centre_circle = plt.Circle((0,0),0.5,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    #plt.show()
    interactive(True)


    data_frame_line = pd.DataFrame(data = csv_data, columns=['Diverted', 'Cancelled','Delayed', 'Year'])
    df = data_frame_line.groupby('Year')['Delayed','Cancelled'].sum()

    ax = df.plot(secondary_y='Delayed', title="Cancelled and Delayed Flights per year")
    ax.set_ylabel('# of Cancelled Flights')
    ax.right_ax.set_ylabel('# of Delayed Flights')

    plt.show()




main("airlines.csv")
