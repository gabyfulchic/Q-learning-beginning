import gym
import IPython

kind_env='FrozenLake8x8-v0'
iter_nbr=10

env = gym.make(kind_env)
env.reset()

# display object attribute > dir(env)

for _ in range(iter_nbr):
    env.render()
    env.step(env.action_space.sample())
env.close()

print(env.action_space.sample())
print(env.observation_space.sample())