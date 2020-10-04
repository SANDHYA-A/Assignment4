# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as matpatches
from matplotlib.patches import Circle


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
x1 = np.linspace(-5,5,100)
y1 = x1
plt.plot(x1, y1, 'r', label='m=1')
x2 = np.linspace(-5,5,100)
y2 = -x2/7
plt.plot(x2, y2, 'g', label='m=-1/7')
x3 = np.linspace(-2,5,100)
y3 = -x3
plt.plot(x3, y3, 'b', label='m=-1')
plt.title('Tangent to a cirlce')
plt.xlabel('x', color='#2254FF')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.axis('equal')


c = np.sqrt(2)
circle = plt.Circle((3,1), c)
ax.add_artist(circle)


plt.savefig('tangent.jpg')

plt.show()





