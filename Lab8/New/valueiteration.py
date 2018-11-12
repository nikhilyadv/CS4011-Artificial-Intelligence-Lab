import numpy as np
import copy

n = 3
a = 5                         #D R U L S
s = n*n
p = np.zeros((a,s,s))
R = np.zeros((s))
R[7] = -1
R[4] = -1.2
R[5] = 1
print("Rewards are - ",R)
Q = np.zeros((s))
y = 0.9 #float(input("Enter discount - "))
#print(p)
def checkbound(i,j):
  if i >= 0 and i < n and j >= 0 and j < n:
    return True
  return False

def checkdiff(v1,v2):
  diff = 0
  for i in range(0,v1.size):
    diff += abs(v1[i]-v2[i])
  return diff

dr = [1,0,-1,0,0]
dc = [0,1,0,-1,0]

for action in range(0,a):
  for i in range(0,n):
    for j in range(0,n):
      neighbours = 0
      for move in range(0,a):
        if checkbound(i+dr[move],j+dc[move]):
          if(move == action):
            p[action][i*n+j][(i+dr[move])*n+j+dc[move]] = 0.7
          else:
              neighbours = neighbours + 1
      for move in range(0,a):
        if checkbound(i+dr[move],j+dc[move]):
          if (move != action and neighbours != 0):
            p[action][i*n+j][(i+dr[move])*n+j+dc[move]] = 0.3 / neighbours
v1 = np.zeros((s))
v = np.ones((s))
e = 1e-10
while checkdiff(v,v1) > e:
  v1 = copy.deepcopy(v) 
  for i in range(0,s):
    maxi = 0
    for action in range(0,a):
      tom = 0
      for j in range(0,s):
        tom += p[action][i][j]*(y*v1[j]+R[j])
      if tom > maxi:
        maxi = tom
    v[i] = maxi

for i in range(0,s):
  maxi = -1
  arg = -1
  for action in range(0,a):
    tom = 0
    for j in range(0,s):
      tom += p[action][i][j]*(y*v1[j]+R[j])
    if tom > maxi:
      maxi = tom
      arg = action
  Q[i] = arg
q = np.chararray((n,n),unicode=True)
for i in range(0,n):
  for j in range(0,n):
    if Q[i*n+j] == 0:
      q[i][j] = 'D'
    elif Q[i*n+j] == 1:
      q[i][j] = 'R'
    elif Q[i*n+j] == 2:
      q[i][j] = 'U'
    elif Q[i*n+j] == 3:
      q[i][j] = 'L'
    else:
      q[i][j] = 'S'
print("Optimal Policy would be -")
print(q)
  