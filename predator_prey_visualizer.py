from predator_prey_model import *

# import numpy and matplotlib
import numpy as np
import matplotlib.pylab as plt
import time
import pylab as pl
import sympy as sy

NUM_ITERATIONS = 200
    
if __name__ == "__main__":
    plt.rcParams['figure.figsize'] = [6, 4]
    fig = plt.figure()

    plt.xlabel("Number of Rabbits")
    plt.ylabel("Number of Foxes")
    
    M = Model(10, 1)
    i=0
    while i < NUM_ITERATIONS:
        i+=1
        print('Cycle number ' + str(i) + ' is running. \n')
        print(M)
        plt.scatter(M.r, M.f, color='red')
        plt.draw()
        M.execute_single_iteration()
    
        plt.pause(0.01)

    plt.show()

