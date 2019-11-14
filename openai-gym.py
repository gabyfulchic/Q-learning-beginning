import gym
import IPython

kind_env = 'FrozenLake8x8-v0'
step_nbr = 20
episode_nbr = 10

env = gym.make(kind_env)
env.reset()
observation = env.reset()

# display object attribute > dir(env) 
# dir(env)
# dir(env.action_space)

for episode in range(episode_nbr):
    observation = env.reset()
    for id in range(step_nbr):
        # affiche le rendu du jeu
        env.render()
        # affiche l'observartion
        print(observation)
        # prepare une action à exec
        action = env.action_space.sample()
        env.step(action)
        # réagir suivant la position et l'avancée
        observation, reward, done, info = env.step(action)
        if done:
            print("Euh bah c'est finit frérot.... après {} pas..".format(id+1))
            break
    env.close()

#print(env.action_space.sample())
#print(env.observation_space.sample())
