import numpy as np
import matplotlib.pyplot as plt

with open("mix_hgts_sort.txt") as f:
	
	lines = f.readlines()[1:]
	

x = [float(line.split()[1]) for line in lines]
y = [float(line.split()[3]) for line in lines]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("PBLH")    
ax1.set_xlabel('hour')
ax1.set_ylabel('mixing hgt')

ax1.plot(x,y, c='r')

leg = ax1.legend()

plt.show()
