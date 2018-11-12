import numpy as np
import math
import matplotlib.pyplot as plt

def geterror():
	return 2*(np.random.random()-0.5)

def alpha(t,k,c):
	return c/(t+k)

iterations = 10000
k = 100
c = 1
theta = np.zeros((iterations,2))
n = theta.shape[1]
b = np.array([1,-1])
A = np.array([[1,0],[0,1]])
thetastar = np.matmul(np.linalg.inv(A),b)
error = np.zeros(iterations)
error[0] = np.linalg.norm((theta[0] - thetastar),ord = 2)

for i in range(1,iterations):
	noise = np.array([geterror(),geterror()])
	theta[i] = theta[i-1] + alpha(i,k,c)*(b - noise - np.matmul(A,theta[i-1]))
	error[i] = np.linalg.norm((theta[i] - thetastar),ord = 2)

print("Thetastar - ",thetastar)
print("Theta - ",theta[iterations-1])
print("Eigen values - ",np.linalg.eigvals(A))
plt.plot(theta[:,0],theta[:,1])
plt.scatter(thetastar[0],thetastar[1],s=100,color="red")
plt.show()
plt.plot(range(iterations),error)
plt.show()