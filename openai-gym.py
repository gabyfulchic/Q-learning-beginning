import gym
import IPython

kind_env='FrozenLake8x8-v0'
iter_nbr=200

env = gym.make(kind_env)
env.reset()
observation = env.reset()

# display object attribute > dir(env) 
# dir(env)
# dir(env.action_space)

for _ in range(iter_nbr):
    env.render()
    # observation = env.reset()
    # print(observation)
    action = env.action_space.sample()
    env.step(action)
    observation, reward, done, info = env.step(action)
    # if done:
    #     print("Euh bah c'est finit frérot.... après {} timesteps".format(t+1))
    #     break
env.close()

#print(env.action_space.sample())
#print(env.observation_space.sample())
