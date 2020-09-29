# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as matpatches
from matplotlib.patches import Circle
#if using termux
import subprocess
import shlex
#end if
#annotate(text, xy, *args, **kwargs)
#Plotting the circle

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
x1 = np.linspace(-2,5,100)
y1 = x1
plt.plot(x1, y1, 'r', label='m=1')
x2 = np.linspace(-2,5,100)
y2 = -x2/7
plt.plot(x2, y2, 'g', label='m=-1/7')
plt.title('Tangent to a cirlce')
plt.xlabel('x', color='#2254FF')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()


c = np.sqrt(2)
circle = plt.Circle((3,1), c)
ax.add_artist(circle)
plt.savefig('tangent.jpg')
'''
theta = np.linspace(0,2*np.pi,50)
x = c*np.cos(theta)
y = c*np.sin(theta)

plt.plot(x,y)

plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#if using termux
#plt.savefig('../figs/circle.pdf')
#plt.savefig('../figs/circle.eps')
#subprocess.run(shlex.split("termux-open ../figs/circle.pdf"))
#else
'''
plt.show()





