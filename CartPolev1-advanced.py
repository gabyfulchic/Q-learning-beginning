import gym
import IPython

kind_env = 'CartPole-v1'
step_nbr = 500
# episode_nbr = 10

env = gym.make(kind_env)
env.reset()

for episode in range(episode_nbr):
    for _ in range(step_nbr):
        # env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print("Step {}:".format(step_index))
        print("Action {}:".format(action))
        print("Observation {}:".format(observation))
        print("Reward {}:".format(reward))
        print("Done {}:".format(done))
        print("Infos {}:".format(info))
        if done:
            print("Euh bah c'est finit frérot.... après {} pas..".format(id+1))
            break
    env.close()

