import gym
import IPython
import random
import numpy as np
from keras.models import Sequential
from keras.models import Dense
from keras.models import Adam

kind_env = 'CartPole-v1'
step_nbr = 500
episode_nbr = 10000
score_requirement = 60

env = gym.make(kind_env)
env.reset()

training_data = []
accepted_score = []

def training_data():
    for episode in range(episode_nbr):
        
        score = 0
        game_memory = []
        previous_observation = []
        
        for step_id in range(step_nbr):
            
            action = random.randrange(0, 2)
            observation, reward, done, info = env.step(action)
            
            if len(previous_observation) > 0:
                game_memory.append([previous_observation, action])
            
            previous_observation = observation
            score += reward
            
            if done:
                print("Euh bah c'est finit frérot.... après {} pas..".format(step_id+1))
                break
        
            if score >= score_requirement:
                accepted_score.append(score)
                for data in game_memory:
                    if data[1] == 1:
                        output = [0, 1]
                    elif data[1] == 0:
                        output = [1, 0]
                    training_data.append([data[0], output])
            
            env.reset()
    
        print(accepted_score)
        return training_data


def build_model(input_size, output_size):
    model = Sequential()
    model.add(Dense(128, input_dim=input_size, activation='relu'))
    model.add(Dense(52, activation='relu'))
    model.add(Dense(output_size, activation='linear'))
    model.compile(loss='mse', optimizer=Adam())

    return model


def train_model(training_data):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
    y = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][1]))
    model = build_model(input_size=len(X[0]), output_size=len(y[0]))

    model.fit(X, y, epochs=10)
    return model


trained_model = train_model(training_data)
