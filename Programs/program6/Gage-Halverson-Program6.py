import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive




def main(file_name):
    csv_data = pd.read_csv(file_name)

    #Pie Chart of types of delays
    data_frame_pie = pd.DataFrame(data = csv_data, columns=['# of Delays.Carrier',\
                                                        '# of Delays.Late Aircraft',\
                                                        '# of Delays.National Aviation System',\
                                                        '# of Delays.Security','# of Delays.Weather']).sum()
    print(data_frame_pie)

    data_frame_pie.plot(kind='pie', autopct='%1.1f%%', labels=None, legend=True)
    plt.show()


    data_frame_line = pd.DataFrame(data = csv_data, columns=['Diverted', 'Cancelled', 'Year'])
    data = data_frame_line.groupby('Year')['Cancelled','Diverted'].sum()
    data.plot(kind='line')
    plt.ylabel("# Cancelled Flights")
    plt.show()




main("airlines.csv")
