#!/usr/bin/env python3

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import MultipleLocator
import time
import numpy as np
import sys
import interactive_legend as il

# plt.style.use('fivethirtyeight')
saveplot = True

x_vals = []
y_vals = []

index = count()

grid_color = 'r'
load_color = 'b'
pv_color = 'g'
battery_color = 'm'
battery_SOC_color = 'c'


topics = ["Inverter/GridWatts","Inverter/LoadWatts","Inverter/PvWattsTotal",
"Inverter/MPPT1_Amps","Inverter/MPPT1_Volts", "Inverter/BatterySOC"]

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = '01_04_2020.csv'
    print("Usage animate_plot.py <filename.csv>")

fig = plt.figure()

lines = []
ax1 = None
ax2 = None


def press(event):
    print('press', event.key)

    if event.key < '9' and event.key >= '1':
        # print("Valid key")
        i = int(event.key) - 1
        visible = lines[i].get_visible()
        lines[i].set_visible(not visible)
        fig.canvas.draw()


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

    # plt.cla()
    # ax1 = plt.subplot(5,1,1)
    # grid_data_x = grid_data['epochTime']
    # ax1.plot(grid_data_x, grid_data['value'], grid_color, label='GridWatts')
    # ax1.legend(loc='best')
    # ax2 = plt.subplot(5,1,2, sharex=ax1, sharey=ax1)
    # ax2.plot(pv_data['epochTime'], pv_data['value'], pv_color, label='PVWatts')
    # ax2.legend(loc='best')
    # ax3 = plt.subplot(5,1,3, sharex=ax2, sharey=ax2)
    # ax3.plot(load_data['epochTime'], load_data['value'], load_color, label='LoadWatts')
    # ax3.legend(loc='best')
    # ax4 = plt.subplot(5,1,4, sharex=ax3, sharey=ax3)
    # ax4.plot(battery_data['epochTime'], battery_data['value'], battery_color, label='BatteryWatts')
    # ax4.legend(loc='best')
    # ax5 = plt.subplot(5,1,5, sharex=ax4)
    # ax5.plot(battery_soc['epochTime'], battery_soc['value'], battery_SOC_color, label='BatterySOC')
    # plt.tight_layout()
    # plt.gcf().autofmt_xdate()

    # plt.grid('on')

    # # plt.gca().xaxis.set_major_locator(mtick.FixedLocator(grid_data_x))
    # plt.gca().xaxis.set_major_formatter(
    # mtick.FuncFormatter(lambda pos,_: time.strftime("%H:%M:%S",time.localtime(pos)))
    # )

    
    # ax4.text(0.1, 0.1,'Records: %d' % len(pv_data),
    #  horizontalalignment='center',
    #  verticalalignment='center',
    #  transform = ax4.transAxes)
    # plt.gcf().set_size_inches(16,9)
    # if saveplot == True:
    #     plt.savefig(filename + ".png", dpi=100)




    # plt.cla()
    ax1 = plt.gca()
    grid_data_x = grid_data['epochTime']
    lines.append(ax1.plot(grid_data_x, grid_data['value'], grid_color, label='GridWatts')[0])
    lines.append(ax1.plot(pv_data['epochTime'], pv_data['value'], pv_color, label='PVWatts')[0])
    lines.append(ax1.plot(load_data['epochTime'], load_data['value'], load_color, label='LoadWatts')[0])
    lines.append(ax1.plot(battery_data['epochTime'], battery_data['value'], battery_color, label='BatteryWatts')[0])

    ax2 = ax1.twinx()

    lines.append(ax2.plot(battery_soc['epochTime'], battery_soc['value'], battery_SOC_color, label='BatterySOC')[0])

    labs = [l.get_label() for l in lines]
    ax1.legend(lines, labs, loc=0)


    ax1.set_ylabel("Power [W]")
    ax2.set_ylabel("Battery SOC [%]")

    plt.tight_layout()
    plt.gcf().autofmt_xdate()

    # plt.gca().xaxis.set_major_locator(mtick.FixedLocator(grid_data_x))
    plt.gca().xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda pos,_: time.strftime("%H:%M:%S",time.localtime(pos)))
    )
    ax1.yaxis.set_major_locator(MultipleLocator(1000))
    ax1.grid(which='major')

    
    ax1.text(0.1, 0.1,'Records: %d' % len(pv_data),
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax1.transAxes)
    plt.gcf().set_size_inches(16,9)
    if saveplot == True:
        plt.savefig(filename + "2.png", dpi=100)

    plt.sca(ax1)


plot_data()
fig.canvas.mpl_connect('key_press_event', press)

plt.tight_layout()
plt.show()
