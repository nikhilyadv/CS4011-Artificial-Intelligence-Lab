import numpy as np
import math
import copy

class Mountain_car:
	def __init__(self):
		self.min_action = -1.0
		self.max_action = 1.0
		self.max_position = 0.6
		self.min_position = -1.2
		self.max_vel = 0.07
		self.min_vel = -0.07
		self.action_space = np.array([-1,0,1])
		self.observational_space_max = np.array([self.max_position,self.max_vel])
		self.observational_space_min = np.array([self.min_position,self.min_vel])
		self.actions = [-1,0,1]
		self.goal = 0.4
	def step(self,action):
		pos = self.state[0]
		vel = self.state[1]
		vel += self.actions[action] * 0.001 + math.cos(3 * pos) * (-0.0025)
		if vel > self.max_vel:
			vel = self.max_vel
		if vel < self.min_vel:
			vel = self.min_vel
		pos += vel
		if pos > self.max_position:
			pos = self.max_position
		if pos < self.min_position:
			pos = self.min_position
		if pos == self.min_position and vel < 0 :
			vel = 0
		done = False
		if pos >= self.goal:
			done = True
		reward = -1.0
		if done:
			reward = 100.0
		#reward -= math.pow(action,2)*0.1
		self.state = np.array([pos,vel])
		return self.state, reward, done
	def reset(self):
		self.state = np.array([np.random.uniform(-0.6, 0.6),0])
		return np.array(self.state)

n_states = 20
actions = 3
iteration_max = 10000
steps = 10000
learning_rate_max = 1.0
learning_rate_min = 0.003
gamma = 1.0				#discount factor
eps = 0.02

def run_episode(envi, policy=None):
	obs = envi.reset()
	total_reward = 0
	step_idx = 0
	for _ in range(steps):
		if policy is None:
			action = envi.action_space.sample()
		else:
			a,b = getstate(envi, obs)
			action = policy[a][b]
		obs, reward, done = envi.step(action)
		total_reward += gamma ** step_idx * reward
		step_idx += 1
		if done:
			break
	return total_reward

def getstate(envi,state):
	dx = (envi.observational_space_max - envi.observational_space_min) / n_states
	a = int((state[0]-envi.observational_space_min[0])/dx[0])
	b = int((state[1]-envi.observational_space_min[1])/dx[1])
	return a , b

envi = Mountain_car()
q_table = np.zeros((n_states,n_states,actions))
for i in range(iteration_max):
	state = envi.reset()
	total_reward = 0
	eta = max(learning_rate_min,learning_rate_max * (0.85 ** (i//100)))
	for j in range(steps):
		p , q = getstate(envi,state)
		if np.random.uniform(0, 1) < eps:
			action = np.random.choice(envi.action_space)
		else:
			logits = q_table[p][q]
			logits_exp = np.exp(logits)
			probs = logits_exp / np.sum(logits_exp)
			action = np.random.choice(envi.action_space, p=probs)
		state , reward , done = envi.step(action)
		total_reward += reward
		r , s = getstate(envi,state)
		q_table[p][q][action] = q_table[p][q][action] + eta * (reward + gamma *  np.max(q_table[r][s]) - q_table[p][q][action])
		if done:
			break
	if i % 100 == 0:
		print('Iteration #%d -- Total reward = %d.' %(i+1, total_reward))
policy = np.argmax(q_table,axis = 2)
solution_policy_scores = [run_episode(envi, policy) for _ in range(100)]
print("Average score of solution = ", np.mean(solution_policy_scores))
