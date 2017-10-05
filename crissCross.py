import numpy as np
import pylab as pl
from matplotlib import collections  as mc

#lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
#c = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lines = [[(0,0),(1,0)]]
c = np.array([(0,0,0,1)])


x1 = 0
y1 = 0
x2 = 1
y2 = 0
CCC = c

for step in range(0,50):
	y2 = y2 + 0.02
	lines.append([(x1,y1),(x2,y2)])
	CCC = np.append(CCC, c, axis=0)
	
x1 = 1
y1 = 0
x2 = 0
y2 = 0

lines.append([(x1,y1),(x2,y2)])
CCC = np.append(CCC,c, axis=0)

for step in range(0,50):
	y2 = y2 + 0.02
	lines.append([(x1,y1),(x2,y2)])
	CCC = np.append(CCC, c, axis=0)


lc = mc.LineCollection(lines, colors=c, linewidths=0.13)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)

pl.show()