import numpy as np

pwicket = np.zeros((10,5))
pstrikerate = np.zeros((10))
def getpwicket():
	pwicket[9][0] = 0.01
	pwicket[9][1] = 0.02
	pwicket[9][2] = 0.03
	pwicket[9][3] = 0.1
	pwicket[9][4] = 0.3
	pwicket[0][0] = 0.1
	pwicket[0][1] = 0.2
	pwicket[0][2] = 0.3
	pwicket[0][3] = 0.5
	pwicket[0][4] = 0.7
	for i in range(1,9):
		for j in range(0,5):
			pwicket[i][j] = pwicket[0][j] + (pwicket[9][j] - pwicket[0][j]) * i / 9
def getstrikerate():
	pstrikerate[9] = 0.8
	pstrikerate[0] = 0.5
	for i in range(1,9):
		pstrikerate[i] = pstrikerate[0] + (pstrikerate[9] - pstrikerate[0]) * i / 9
getpwicket()
getstrikerate()

numballs = 300
wickets = 10

v = np.zeros((numballs+1,wickets))
shot = np.zeros((numballs+1,wickets))

def getrun(i):
	if i == 0:
		return 1
	if i == 1:
		return 2
	if i == 2:
		return 3
	if i == 3:
		return 4
	if i == 4:
		return 6
def bellman(ballsleft,wicketsinhand):
	if ballsleft == 0:
		return 0 , -1
	maximum = -1
	action = -1
	for i in range(0,5):
		if wicketsinhand != 0:
			value = (1-pwicket[wicketsinhand][i]) * (pstrikerate[wicketsinhand] * getrun(i) + v[ballsleft-1][wicketsinhand]) + pwicket[wicketsinhand][i] * v[ballsleft-1][wicketsinhand-1]
		else:
			value = (1-pwicket[wicketsinhand][i]) * (pstrikerate[wicketsinhand] * getrun(i) + v[ballsleft-1][wicketsinhand])
		if (value > maximum):
			maximum = value
			action = getrun(i)
	return maximum,action

for i in range(1,numballs+1):
	for j in range(0,wickets):
		v[i][j] , shot[numballs-i][j] = bellman(i,j)
np.savetxt("value.txt",v[1:numballs+1],fmt = '%2.6f')
np.savetxt("shot.txt",shot[0:numballs],fmt = '%0.f')

