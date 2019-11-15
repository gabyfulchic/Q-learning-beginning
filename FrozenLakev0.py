import os, pickle, time
import gym
import numpy
import random

kind_env = 'FrozenLake-v0'
max_steps = 200
total_episodes = 10000
epsilon = 0.9
l_rate = 0.81
gamma = 0.96

env = gym.make(kind_env)
env.reset()
observation = env.reset()

def choose_action(action):
    action = 0
    if numpy.random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = numpy.argmax(Q[state, :])
    return action

def learn(state, state2, reward, action):
    predict = Q[state, action]
    target = reward + gamma * numpy.max(Q[state2, :])
    Q[state, action] = Q[state, action] + l_rate * (target - predict)

def trash():
    for episode in range(total_episodes):
        observation = env.reset()
        for step in range(max_steps):
            # affiche le rendu du jeu
            env.render()
            
            # prepare une action à exec
            current_state = observation
            random_action = env.action_space.sample()
            
            if random_action < epsilon:
                env.step(random_action)
                observation, reward, done, info = env.step(random_action)
                epsilon += 1  
            
            # réagir suivant la position et l'avancée
            if done:
                print("Perdu après {} steps !! ".format(step+1))
                break
        env.close()

########
# main #
########

Q = numpy.zeros((env.observation_space.n, env.action_space.n))

for episode in range(total_episodes):
    state = env.reset()
    t = 0
    while t < max_steps:
        env.render()
        action = choose_action(state)
        state2, reward, done, info = env.step(action)
        learn(state, state2, reward, action)
        state = state2
        t += 1
        if done:
            break
        time.sleep(0.1)

print(Q)
