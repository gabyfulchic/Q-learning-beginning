import gym
import IPython
import random
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

kind_env = 'CartPole-v1'
step_nbr = 500
episode_nbr = 10000
score_requirement = 160

env = gym.make(kind_env)
env.reset()

training_data = []
accepted_score = []

def get_trained_model(training_data):
    
    
    return trained_model

def get_training_data(trained_model):
    for episode in range(episode_nbr):
        
        score = 0
        prev_obs = []
        choices = []
        
        for step_id in range(step_nbr):
            
            if len(prev_obs) == 0:
                action = random.randrange(0, 2)
            else:
                action = np.argmax(trained_model.predict(prev_obs.reshape(-1, len(prev_obs)))[0])

            choices.append(action)
            new_observation, reward, done, info = env.step(action)
            prev_obs = new_observation
            score += reward
            
            if done:
                break
        
            if score >= score_requirement:
                accepted_score.append(score) 
           
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


get_training_data()
trained_model = train_model(training_data)
