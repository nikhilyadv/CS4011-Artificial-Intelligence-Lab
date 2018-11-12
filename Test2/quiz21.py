import numpy as np
import matplotlib.pyplot as plt
import random

wickets = 3
overs = 10
economy = [3,3.5,4,4.5,5]
strike = [33,30,24,18,15]

v = np.zeros((wickets + 1, overs + 1, (1<<10)))
action = np.zeros((wickets + 1, overs + 1, (1<<10)))

def dp(wicketsleft,oversleft,b):
	if wicketsleft == 0 or oversleft == 0:
		return 0
	if v[wicketsleft][oversleft][b]:            #check not 0
		return v[wicketsleft][oversleft][b]
	m1 = -1
	m2 = np.inf
	for i in range(10):
		m = b ^ int(1<<i)
		if b & int(1<<i):
			bolwer = (i)//2
			pout = 6 / strike[bolwer]
			value = economy[bolwer] + pout * dp(wicketsleft - 1,oversleft - 1,m) + (1 - pout) * dp(wicketsleft,oversleft - 1,m)
			if value < m2:
				m2 = value
				m1 = i
	v[wicketsleft][oversleft][b] = m2
	action[wicketsleft][oversleft][b] = m1
	return v[wicketsleft][oversleft][b]

def simulate(wicketsleft,oversleft):
	run = 0
	o = [2,2,2,2,2]
	b = (1<<10)-1
	for i in range(overs):
		if wicketsleft == 0:
			print("Game Over")
			break
		#print(wicketsleft,oversleft,b)
		bolwer = int(action[wicketsleft][oversleft][b]/2)
		print("Overs - ", i + 1,"\taction - ",bolwer)
		b = b ^ int(1 << int(action[wicketsleft][oversleft][b]))
		prob = random.random()
		run += economy[bolwer]
		if prob <= (6/strike[bolwer]):
			print("wicket")
			wicketsleft -= 1
		oversleft -= 1
	return run

def main():
	dp(3,10,(1<<10)-1)
	avg = 0
	for i in range(1000):
		print("Game - ",i+1)
		temp = simulate(3,10)
		avg += temp
	print(avg/1000)
	print(dp(3,10,(1<<10)-1))
	print(action.tolist())

if __name__ == "__main__":
	main()