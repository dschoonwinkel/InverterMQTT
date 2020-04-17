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
saveplot = True

x_vals = []
y_vals = []

index = count()

topics = ["Inverter/GridWatts","Inverter/LoadWatts","Inverter/PvWattsTotal",
"Inverter/MPPT1_Amps","Inverter/MPPT1_Volts", "Inverter/BatterySOC"]

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = '01_04_2020.csv'
    print("Usage animate_plot.py <filename.csv>")

def plot_data():
    data = pd.read_csv(filename)

    # print(data)
    grid_data = data.loc[data['topic']=='Inverter/GridWatts']
    pv_data = data.loc[data['topic']=='Inverter/PvWattsTotal']
    load_data = data.loc[data['topic']=='Inverter/LoadWatts']
    battery_data = data.loc[data['topic']=='Inverter/BatteryWatts']
    battery_soc = data.loc[data['topic']=='Inverter/BatterySOC']
	# print(grid_data[['epochTime', 'value']])

    # x = data['x_value']
    # y1 = data['total_1']
    # y2 = data['total_2']

    plt.cla()
    ax1 = plt.subplot(5,1,1)
    grid_data_x = grid_data['epochTime']
    ax1.plot(grid_data_x, grid_data['value'], 'k', label='GridWatts')
    ax1.legend(loc='best')
    ax2 = plt.subplot(5,1,2, sharex=ax1, sharey=ax1)
    ax2.plot(pv_data['epochTime'], pv_data['value'], 'b', label='PVWatts')
    ax2.legend(loc='best')
    ax3 = plt.subplot(5,1,3, sharex=ax2, sharey=ax2)
    ax3.plot(load_data['epochTime'], load_data['value'], 'r', label='LoadWatts')
    ax3.legend(loc='best')
    ax4 = plt.subplot(5,1,4, sharex=ax3, sharey=ax3)
    ax4.plot(battery_data['epochTime'], battery_data['value'], 'y', label='BatteryWatts')
    ax4.legend(loc='best')
    ax5 = plt.subplot(5,1,5, sharex=ax4)
    ax5.plot(battery_soc['epochTime'], battery_soc['value'], 'c', label='BatterySOC')
    plt.tight_layout()
    plt.gcf().autofmt_xdate()

    # plt.gca().xaxis.set_major_locator(mtick.FixedLocator(grid_data_x))
    plt.gca().xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda pos,_: time.strftime("%H:%M:%S",time.localtime(pos)))
    )

    
    ax4.text(0.1, 0.1,'Records: %d' % len(pv_data),
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax4.transAxes)
    plt.gcf().set_size_inches(16,9)
    if saveplot == True:
        plt.savefig(filename + ".png", dpi=100)

    fig = plt.figure()
    # plt.cla()
    ax1 = plt.gca()
    grid_data_x = grid_data['epochTime']
    ax1.plot(grid_data_x, grid_data['value'], 'k', label='GridWatts')
    ax1.plot(pv_data['epochTime'], pv_data['value'], 'b', label='PVWatts')
    ax1.plot(load_data['epochTime'], load_data['value'], 'r', label='LoadWatts')
    ax1.plot(battery_data['epochTime'], battery_data['value'], 'y', label='BatteryWatts')

    ax2 = ax1.twinx()

    ax2.plot(battery_soc['epochTime'], battery_soc['value'], 'c', label='BatterySOC')

    ax1.legend()

    ax1.set_ylabel("Watts")
    ax2.set_ylabel("Battery SOC [%]")

    plt.tight_layout()
    plt.gcf().autofmt_xdate()

    # plt.gca().xaxis.set_major_locator(mtick.FixedLocator(grid_data_x))
    plt.gca().xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda pos,_: time.strftime("%H:%M:%S",time.localtime(pos)))
    )

    
    ax1.text(0.1, 0.1,'Records: %d' % len(pv_data),
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax4.transAxes)
    plt.gcf().set_size_inches(16,9)
    if saveplot == True:
        plt.savefig(filename + "2.png", dpi=100)


# ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plot_data()

plt.tight_layout()
plt.show()
