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
if random.uniform(0,1) < 0.95:
	c[0][3] = random.uniform(.48,.52)
else: 
	c[0][3] = 1
CC = c
c = np.array([(0,0,1,1)]) # blue
random.shuffle(c[0])
if random.uniform(0,1) < 0.95:
	c[0][3] = random.uniform(.48,.52)
else: 
	c[0][3] = 1
CC = np.append(CC, c, axis=0)
c = np.array([(0,1,.8,1)]) # green
random.shuffle(c[0])
if random.uniform(0,1) < 0.95:
	c[0][3] = random.uniform(.48,.52)
else: 
	c[0][3] = 1
CC = np.append(CC, c, axis=0)
c = np.array([(1,1,.8,1)]) # yellow
random.shuffle(c[0])
if random.uniform(0,1) < 0.95:
	c[0][3] = random.uniform(.48,.52)
else: 
	c[0][3] = 1
CC = np.append(CC, c, axis=0)
c = np.array([(1,0,.8,1)]) # red
random.shuffle(c[0])
if random.uniform(0,1) < 0.95:
	c[0][3] = random.uniform(.48,.52)
else: 
	c[0][3] = 1
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

octDraw = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def lineDraw(x1, y1, x2, y2, colorVec, counter):
	global CCC
	global cCounter
	CCC = np.append(colorVec, [CC[cCounter]], axis=0)
	lines.append([(x1,y1),(x2,y2)])
	cCounter = (counter + 1) % 5
	return
	
m = random.uniform(0,1)
iter = 23 + random.randrange(289)
thickness = 100 * random.uniform(0,1.5)

# 50% chance upper is 1, 50% chance lower is 0 
if random.uniform(0,1) < 0.5:
	upper = 1
else:	
	upper = random.uniform(0.5,1)
	
if random.uniform(0,1) < 0.5:
	lower = 0
else:	
	lower = random.uniform(0,0.5)
	
		

def mFactor(powerDown, powerUp):
	return(m**random.uniform(powerDown, powerUp)*step)

def A():
	lineDraw(x1=0, y1=0, x2=1, y2=0 + mFactor(lower, upper), colorVec=CCC, counter=cCounter) # A
	return

def B():
	lineDraw(x1=0, y1=0, x2=1 - mFactor(lower, upper), y2=1, colorVec=CCC, counter=cCounter) # B
	return

def C():
	lineDraw(x1=1, y1=0, x2=1 - mFactor(lower, upper), y2=1, colorVec=CCC, counter=cCounter) # C
	return

def D():
	lineDraw(x1=1, y1=0, x2=0, y2=1 - mFactor(lower, upper), colorVec=CCC, counter=cCounter) # D
	return

def E():
	lineDraw(x1=1, y1=1, x2=0, y2=1 - mFactor(lower, upper), colorVec=CCC, counter=cCounter) # E
	return

def F():
	lineDraw(x1=1, y1=1, x2=0 + mFactor(lower, upper), y2=0, colorVec=CCC, counter=cCounter) # F
	return

def G():
	lineDraw(x1=0, y1=1, x2=0 + mFactor(lower, upper), y2=0, colorVec=CCC, counter=cCounter) # G
	return

def H():
	lineDraw(x1=0, y1=1, x2=1, y2=1 + mFactor(lower, upper), colorVec=CCC, counter=cCounter) # H
	return


for step in range(0,iter):
	random.shuffle(octDraw) # randomize order of draws, maybe make this happen every N times for pronounced segments
	for fnStr in octDraw:
		locals()[fnStr]()   # call A-H in their randomized order 

lc = mc.LineCollection(lines, colors=CCC, linewidths=thickness)
fig, ax = pl.subplots()

# pl.axis('tight')
pl.axis('off')
ax.add_collection(lc)
fig.set_size_inches(14, 14)
pl.savefig('rainbow.png', pad_inches=-0.31, bbox_inches='tight')
pl.show()