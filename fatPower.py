import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import matplotlib
import random


#lines = [[(0, 1), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
#c = np.array([(0, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lines = [[(0,0),(1,0)]]
c = np.array([(0.58,0,0.83,1)]) # purple
random.shuffle(c[0])
c[0][3] = .5
CC = c
c = np.array([(0,0,1,1)]) # blue
random.shuffle(c[0])
c[0][3] = .5
CC = np.append(CC, c, axis=0)
c = np.array([(0,1,.8,1)]) # green
random.shuffle(c[0])
c[0][3] = .5
CC = np.append(CC, c, axis=0)
c = np.array([(1,1,.8,1)]) # yellow
random.shuffle(c[0])
c[0][3] = .5
CC = np.append(CC, c, axis=0)
c = np.array([(1,0,.8,1)]) # red
random.shuffle(c[0])
c[0][3] = .5
CC = np.append(CC, c, axis=0)

#lines = [[(0,0),(1,0)]]
#c = np.array([(0.58,0,0.83,1)]) # purple
#CC = c
#c = np.array([(0,0,1,1)]) # blue
#CC = np.append(CC, c, axis=0)
#c = np.array([(0,1,0,1)]) # green
#CC = np.append(CC, c, axis=0)
#c = np.array([(1,1,0,1)]) # yellow
#CC = np.append(CC, c, axis=0)
#c = np.array([(1,0,0,1)]) # red
#CC = np.append(CC, c, axis=0)

CCC = [CC[0]]
cCounter = 0

def lineDraw(x1, y1, x2, y2, colorVec, counter):
	global CCC
	global cCounter
	CCC = np.append(colorVec, [CC[cCounter]], axis=0)
	lines.append([(x1,y1),(x2,y2)])
	cCounter = (counter + 1) % 5
	return
	
m = 0.062
iter = 231
thickness = 114.751

for step in range(0,iter):
	lineDraw(x1=0, y1=0, x2=1, y2=0 + (m**0.8)*step, colorVec=CCC, counter=cCounter) # A
	lineDraw(x1=0, y1=0, x2=1 - (m**0.8)*step, y2=1, colorVec=CCC, counter=cCounter) # B
	lineDraw(x1=1, y1=0, x2=1 - (m**0.8)*step, y2=1, colorVec=CCC, counter=cCounter) # C
	lineDraw(x1=1, y1=0, x2=0, y2=1 - (m**0.8)*step, colorVec=CCC, counter=cCounter) # D
	lineDraw(x1=0, y1=1, x2=1, y2=1 + (m**0.8)*step, colorVec=CCC, counter=cCounter) # H
	lineDraw(x1=0, y1=1, x2=0 + (m**0.8)*step, y2=0, colorVec=CCC, counter=cCounter) # G
	lineDraw(x1=1, y1=1, x2=0 + (m**0.8)*step, y2=0, colorVec=CCC, counter=cCounter) # F
	lineDraw(x1=1, y1=1, x2=0, y2=1 - (m**0.8)*step, colorVec=CCC, counter=cCounter) # E

lc = mc.LineCollection(lines, colors=CCC, linewidths=thickness)
fig, ax = pl.subplots()
fig.set_size_inches(24, 24)
ax.add_collection(lc)
pl.axis('off')
pl.savefig('sendPlaidstel.png', pad_inches=0, bbox_inches='tight')
pl.show()