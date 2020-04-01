import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

topics = ["Inverter/GridWatts","Inverter/LoadWatts","Inverter/PvWattsTotal",
"Inverter/MPPT1_Amps","Inverter/MPPT1_Volts"]


def animate(i):
    data = pd.read_csv('data.csv')

    grid_data = data.loc[data['topic']=='Inverter/GridWatts']
    pv_data = data.loc[data['topic']=='Inverter/PvWattsTotal']
	# print(grid_data[['epochTime', 'value']])

    # x = data['x_value']
    # y1 = data['total_1']
    # y2 = data['total_2']

    plt.cla()

    plt.plot(grid_data['epochTime'], grid_data['value'], label='GridWatts')
    plt.plot(pv_data['epochTime'], pv_data['value'], label='PVWatts')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()