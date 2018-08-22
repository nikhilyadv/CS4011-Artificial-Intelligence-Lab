import numpy as np
np.set_printoptions(threshold=np.inf)

class segtree:
	def __init__(self,arr,n):
		self.n = n
		self.a = np.zeros(100)
		for i in range(0,n):
			self.a[n+i] = arr[i]
		self.build()

	def build(self):
		for i in range(self.n-1,0,-1):
			self.a[i] = self.a[i<<1] + self.a[i<<1 | 1]

	def update(self,index,value):
		index += self.n
		self.a[index] = value
		i = index
		while i > 1:
			self.a[i>>1] = self.a[i] + self.a[i^1]
			i >>= 1


	def query(self,l,r):		#from l to r-1
		res = 0
		l += self.n
		r += self.n
		while l < r:
			if l&1 :
				res += self.a[l]
				l += 1
			if r&1 :
				r -= 1
				res += self.a[r]
			l >>= 1
			r >>= 1
		return res

a = [1,2,3,4,5,6,7,8,9,10,11,12]
seg = segtree(a,12)
print(seg.query(1,3))