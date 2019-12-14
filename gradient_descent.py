import random as rd # random int generator
import pandas as pd # dataset manipulations
import numpy as np # manipulations de tableaux
import pdb # python debugger {pdb.set_trace()}
import matplotlib.pyplot as plt # display graphs
import seaborn as sea # setup statisticals graphics
from scipy import stats # calculs sceintiques


file_name = "univariate_linear_regression_dataset.csv"

def visualize_graphics(file_name, X, Y):
    sea.set()
    datas = sea.load_dataset("dots")
    graph = sea.relplot(x="time", y="firing_rate", col="align", hue="choice", size="coherence", style="choice", facet_kws=dict(sharex=False), kind="line", legend="full", data=datas)
    plt.show(graph)

def set_parameters():
    dataset = pd.read_csv(file_name)
    X = dataset.iloc[:,0]
    Y = dataset.iloc[:,1]
    m = np.shape(X)
    theta = np.ones(m)
    alpha = 0.1
    iterIndex = 100000
    return X, Y, alpha, theta, m, iterIndex

def gradient_descent(X, Y, theta, alpha, m, iterIndex):
    xTrans = x.transpose()
    for i in range(0, iterIndex):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta

def main():
    X, Y, theta, alpha, m, iterIndex = set_parameters()
    visualize_graphics(file_name, X, Y)
    # X, Y, theta, alpha, m, iterIndex = gradient_descent()

if __name__ == '__main__':
    main()

# def debug_function():
#     set_parameters()
#     print("-----------X------------")
#     print(X)
#     print("-----------Y------------")
#     print(Y)
#     print("-----------Theta------------")    
#     print(theta)
#     print("-----------Alpha------------")
#     print(alpha)
#     print("-----------m------------")
#     print(m)
#     print("-----------iterIndex------------")
#     print(iterIndex)
 
