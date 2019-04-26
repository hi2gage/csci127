import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


csv_data = pd.read_csv("airlines.csv")
data_frame_line = pd.DataFrame(data = csv_data, columns=['Diverted', 'Cancelled','Delayed', 'Year'])
df = data_frame_line.groupby('Year')['Delayed','Cancelled'].sum()

ax = df.plot(secondary_y='Delayed')
ax.set_ylabel('# of Cancelled Flights')
ax.right_ax.set_ylabel('# of Delayed Flights')

plt.show()
