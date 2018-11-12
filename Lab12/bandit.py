import numpy as np
import math
import matplotlib.pyplot as plt

k = 5
iterations = 50000
ti = 0
mean = np.zeros(k)
sum = np.zeros(k)
N = np.zeros(k)
nt = np.zeros((k,iterations))
ucb = np.zeros(k)
p = np.ones(k)
for i in range(k):
	p[i] *= np.random.random()

def dis(num):
	prob = np.random.random()
	if prob < p[num]:
		return 1
	return 0

def draw(num):
	global ti
	rv = dis(num)
	N[num] += 1
	sum[num] += rv
	mean[num] = sum[num]/N[num]
	for i in range(k):
		nt[i][ti] = N[i]
	ti += 1

def cal_ucb(t):
	for i in range(k):
		ucb[i] = mean[i] + math.sqrt(2*(np.log(t)/N[i]))

def argmax():
	mx = -1
	index = -1
	for i in range(k):
		if mx < ucb[i]:
			mx = ucb[i]
			index = i
	return index

def print_graph():
	logt = np.zeros(iterations)
	for i in range(iterations-1):
		logt[i+1] = np.log(i+1)
	mx = -1
	index = -1
	for i in range(k):
		if(mean[i] > mx):
			mx = mean[i]
			index = i
	delta = np.zeros(k)
	for i in range(k):
		delta[i] = mx - mean[i]
	for i in range(k):
		if index == i:
			continue
		print(i+1," -> ",8/delta[i],end="\t")
	for i in range(k):
		if index == i:
			continue
		plt.plot(logt,nt[i])
	print()
	for i in range(k):
		if index == i:
			continue
		slope = (N[i] - 0)/(logt[iterations-1]-logt[1])
		print(i+1," -> ",slope,end="\t")
	print()
	plt.show()

def main():
	# pull ones
	for i in range(k):
		draw(i)
	for i in range(k,iterations):
		cal_ucb(i)
		action = argmax()
		draw(action)

	print("Mean - ")
	print(mean)
	print("Probability array - ")
	print(p)
	print_graph()

if __name__ == '__main__':
	main()