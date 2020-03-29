#/usr/bin/env python3
import os

os.remove("plot.dat")

 
def writedata():
    for i in range(1,20):
    	with open("plot.dat", 'a') as file:
    		file.write("%d %d" % (i,i))
        time.sleep(1)
        print("Done")

writedata &
sleep 1
# gnuplot liveplot.gnu