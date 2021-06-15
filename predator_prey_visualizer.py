from predator_prey_model import *

# import numpy and matplotlib
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import time
import pylab as pl
import sympy as sy

NUM_ITERATIONS = 200
    
if __name__ == "__main__":
    plt.rcParams['figure.figsize'] = [6, 4]
    fig = plt.figure()

    plt.xlabel("Number of Rabbits")
    plt.ylabel("Number of Foxes")

    colourmap=cm.get_cmap('viridis', 512)
    
    M = Model(10, 1)
    i=0
    while i < NUM_ITERATIONS:
        i+=1
        print('Cycle number ' + str(i) + ' is running. \n')
        print(M)
        plt.scatter(M.r, M.f, c='red')
        if (i%5==0):
            plt.draw()
            plt.pause(0.005)
        M.execute_single_iteration()
        if (i%100==0):
            plt.clf()
    
        
    plt.show()

