"""
.___                              __   
|   | _____ ______   ____________/  |_ 
|   |/     \\____ \ /  _ \_  __ \   __\
|   |  Y Y  \  |_> >  <_> )  | \/|  |  
|___|__|_|  /   __/ \____/|__|   |__|  
          \/|__|                        
"""

import os, pickle, time
import gym
import numpy as np
import random
import multiprocessing as mp


"""
   _    _      _        ___   _  _   _  _   ___  _____   ___   ____   _  _    ___  
  )_\  ) |    ) |      ) __( ) () ( ) \/ ( / _( )__ __( )_ _( / __ \ ) \/ (  (  _( 
 /( )\ | (__  | (__    | _)  | \/ | |  \ | ))_    | |   _| |_ ))__(( |  \ |  _) \  
)_/ \_()____( )____(   )_(   )____( )_()_( \__(   )_(  )_____(\____/ )_()_( )____) 
                                                                                   
"""

kind_env = 'FrozenLake-v0'
max_steps = 100
total_episodes = 10000
epsilon = 0.5
l_rate = 0.81
gamma = 0.96

env = gym.make(kind_env)
env.reset()

def choose_action(Q, state):
    action = 0
    if np.random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])
    return action

def learn(Q, state, state2, reward, action):
    target = Q[state, action]
    predict = reward + gamma * np.max(Q[state2, :])
    Q[state, action] = Q[state, action] + l_rate * (target - predict)

def save_model(model):
    model_file_name = 'frozenlake_model.sav'
    pickle.dump(model, open(model_file_name, 'wb'))

def load_model(model_name):
    if ".sav" not in model_name:
        model_file_name = model_name+".sav"
        loaded_model = pickle.load(open(model_name))
    else:
        loaded_model = pickle.load(open(model_name))


"""
   _____         .__        
  /     \ _____  |__| ____  
 /  \ /  \\__  \ |  |/    \ 
/    Y    \/ __ \|  |   |  \
\____|__  (____  /__|___|  /
        \/     \/        \/ 

"""

def main(env, max_steps, total_episodes, epsilon, l_rate, gamma):
       
    t0 = time.time()
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    
    for episode in range(total_episodes):
        
        state = env.reset()
        t = 0
        current_progressing = episode / total_episodes * 100
        print("%.2f" % current_progressing+" % ...")
        
        while t < max_steps:
            # env.render()
            action = choose_action(Q, state)
            state2, reward, done, info = env.step(action)
            learn(Q, state, state2, reward, action)
            state = state2
            t += 1
            l_rate = 0.999 * l_rate
            epsilon = 0.98 * epsilon
            if done:
                break
            # pool.close()
    
    print(Q)
    print('That took {} seconds'.format(time.time() - t0))


if __name__ == "__main__":
    main(env, max_steps, total_episodes, epsilon, l_rate, gamma)
