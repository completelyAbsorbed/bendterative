import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import matplotlib


#lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
#c = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lines = [[(0,0),(1,0)]]
c = np.array([(0.58,0,0.83,1)]) # purple
CC = c
c = np.array([(0,0,1,1)]) # blue
CC = np.append(CC, c, axis=0)
c = np.array([(0,1,0,1)]) # green
CC = np.append(CC, c, axis=0)
c = np.array([(1,1,0,1)]) # yellow
CC = np.append(CC, c, axis=0)
c = np.array([(1,0,0,1)]) # red
CC = np.append(CC, c, axis=0)

CCC = [CC[0]]
cCounter = 0

def lineDraw(x1, y1, x2, y2, colorVec, counter):
	global CCC
	global cCounter
	CCC = np.append(colorVec, [CC[cCounter]], axis=0)
	lines.append([(x1,y1),(x2,y2)])
	cCounter = (counter + 1) % 5
	return
	
m = 0.002
iter = 331
thickness = 1.85

for step in range(0,iter):
	lineDraw(x1=0, y1=0, x2=1, y2=0 + m*step, colorVec=CCC, counter=cCounter) # A
	lineDraw(x1=0, y1=0, x2=1 - m*step, y2=1, colorVec=CCC, counter=cCounter) # B
	lineDraw(x1=1, y1=0, x2=1 - m*step, y2=1, colorVec=CCC, counter=cCounter) # C
	lineDraw(x1=1, y1=0, x2=0, y2=1 - m*step, colorVec=CCC, counter=cCounter) # D
	lineDraw(x1=1, y1=1, x2=0, y2=1 - m*step, colorVec=CCC, counter=cCounter) # E
	lineDraw(x1=1, y1=1, x2=0 + m*step, y2=0, colorVec=CCC, counter=cCounter) # F
	lineDraw(x1=0, y1=1, x2=0 + m*step, y2=0, colorVec=CCC, counter=cCounter) # G
	lineDraw(x1=0, y1=1, x2=1, y2=1 + m*step, colorVec=CCC, counter=cCounter) # H

lc = mc.LineCollection(lines, colors=CCC, linewidths=thickness)
fig, ax = pl.subplots()
fig.set_size_inches(13.5, 13.5)
ax.add_collection(lc)
pl.axis('off')
pl.savefig('rainbow.png', pad_inches=0, bbox_inches='tight')
pl.show()