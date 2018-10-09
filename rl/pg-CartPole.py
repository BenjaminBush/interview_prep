'''
Policy gradient numpy implementation for OpenAI Gym CartPole environment
Adapted From: https://gist.github.com/karpathy/a4166c7fe253700972fcbc77e4ea32c5
'''
import gym
import numpy as np

# hyperparameters
D = 4					# Input dimensionality
H = 10					# Number of hidden nodes
gamma = 0.99			# Decay Rate
learning_rate = 1e-2	# Learning Rate

num_rollouts = 1000
test_cases = 100


model = {}
model['W1'] = np.random.randn(H, D)/np.sqrt(D)
model['W2'] = np.random.randn(H)/np.sqrt(H)

def sigmoid(s):
	return (1.0/(1.0 + np.exp(-s)))

def discount_rewards(ep_rewards):
	ep_discounted_rewards = np.zeros_like(ep_rewards)
	running_add = 0
	for t in reversed(range(0, ep_rewards.size)):
		running_add = ep_rewards[t] + (running_add*gamma)
		ep_discounted_rewards[t] = running_add
	return ep_discounted_rewards


# @param x: An observation: [position of cart, velocity of cart, angle of pole, rotation rate of pole]
def policy_forward(x):
	h = np.dot(model['W1'], x) 
	h[h<0] = 0					# ReLu
	logp = np.dot(model['W2'], h)	# Hiddent state
	p = sigmoid(logp)				# Probability
	return p, h 				# Return probability of selecting action 1, and hidden state

def policy_backward(ep_hidden, ep_probs, ep_obs):
	dW2 = np.dot(ep_hidden.T, ep_probs).ravel()
	dh = np.outer(ep_probs, model['W2'])
	dh[ep_hidden<=0] = 0
	dW1 = np.dot(dh.T, ep_obs)
	return {'W1':dW1, 'W2': dW2}


observations, hidden_states, rewards, probs = [], [], [], []

reward_sum = 0

env = gym.make("CartPole-v0")
observation = env.reset()

#Training
for episode in range(0, num_rollouts):
	observation = env.reset()

	while True:
		x = observation
		observations.append(x)

		# Forward pass
		p, hidden_s = policy_forward(x)
		hidden_states.append(hidden_s)


		# Calculate action and fake label
		action = 1 if np.random.uniform() < p else 0
		fake_label = 1 if action == 1 else 0

		probs.append(fake_label - p)

		# Take the action, get new measurements
		observation, reward, done, info = env.step(action)

		reward_sum += reward
		rewards.append(reward_sum)

		if done or reward_sum > 200:
			# Record the episode information
			ep_obs = np.vstack(observations)
			ep_hidden = np.vstack(hidden_states)
			ep_probs = np.vstack(probs)
			ep_rewards = np.vstack(rewards)

			# Reset episode information
			observations, hidden_states, rewards, probs = [], [], [], []

			# Compute discounted rewards
			ep_discounted_rewards = discount_rewards(ep_rewards)

			# Normalize discounted rewards
			ep_discounted_rewards -= np.mean(ep_discounted_rewards)
			ep_discounted_rewards /= np.std(ep_discounted_rewards)

			# Multiply rewards by the prob policy
			ep_probs *= ep_discounted_rewards

			grad = policy_backward(ep_hidden, ep_probs, ep_obs)

			for k, v in model.items():
				model[k] += learning_rate*grad[k]

			reward_sum = 0
			observation = env.reset()
			break


# Testing
test_reward = 0
for i in range(0, test_cases):
	iter = 0
	reward_sum = 0
	observation = env.reset()
	while True:
                env.render()
		p, h = policy_forward(observation)
		action = 1 if np.random.uniform() < p else 0

		observation, reward, done, info = env.step(action)

		reward_sum += reward
		iter += 1
		if done or iter > 300:
			test_reward += reward_sum
			iter = 0
			reward_sum = 0
			break

average_score = float(test_reward/test_cases)
print("We averaged a score of {} across {} test instances".format(average_score, test_cases))
