#!/usr/bin/env python3

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.animation import FuncAnimation
import time
import numpy as np
import sys

plt.style.use('fivethirtyeight')
saveplot = False

x_vals = []
y_vals = []

index = count()

topics = ["Inverter/GridWatts","Inverter/LoadWatts","Inverter/PvWattsTotal",
"Inverter/MPPT1_Amps","Inverter/MPPT1_Volts"]

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = '01_04_2020.csv'
    print("Usage animate_plot.py <filename.csv>")

def animate(i):
    data = pd.read_csv(filename)

    # print(data)
    grid_data = data.loc[data['topic']=='Inverter/GridWatts']
    pv_data = data.loc[data['topic']=='Inverter/PvWattsTotal']
    load_data = data.loc[data['topic']=='Inverter/LoadWatts']
    battery_data = data.loc[data['topic']=='Inverter/BatteryWatts']
	# print(grid_data[['epochTime', 'value']])

    # x = data['x_value']
    # y1 = data['total_1']
    # y2 = data['total_2']

    plt.viridis()
    plt.cla()
    ax = plt.gca()

    grid_data_x = grid_data['epochTime']

    ax.plot(grid_data_x, grid_data['value'], 'k', label='GridWatts')
    ax.plot(pv_data['epochTime'], pv_data['value'], label='PVWatts')
    ax.plot(load_data['epochTime'], load_data['value'], label='LoadWatts')
    ax.plot(battery_data['epochTime'], battery_data['value'], label='BatteryWatts')

    ax.legend(loc='best')
    plt.tight_layout()
    plt.gcf().autofmt_xdate()

    # plt.gca().xaxis.set_major_locator(mtick.FixedLocator(grid_data_x))
    plt.gca().xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda pos,_: time.strftime("%H:%M:%S",time.localtime(pos)))
    )

    
    ax.text(0.1, 0.1,'Records: %d' % len(pv_data),
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax.transAxes)
    if saveplot == True:
        plt.gcf().set_size_inches(16,9)
        plt.savefig(filename + ".png", dpi=100)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
