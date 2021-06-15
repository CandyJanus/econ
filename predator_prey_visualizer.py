from predator_prey_model import *

# import numpy and matplotlib
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import time
import pylab as pl
import sympy as sy

NUM_ITERATIONS = 1000
    
MAX_PTS_SHOWN = 25


if __name__ == "__main__":
    plt.rcParams['figure.figsize'] = [6, 4]
    fig = plt.figure()

    plt.xlabel("Number of Rabbits")
    plt.ylabel("Number of Foxes")
    plt.xlim((-20, 600))
    plt.ylim((-20, 600))

    colourmap=cm.get_cmap('viridis', 512)
    
    M = Model(10, 1)
    i=0
    
    current_pts = []
    all_pts = []

    while i < NUM_ITERATIONS:
        i+=1
        print('Cycle number ' + str(i) + ' is running. \n')
        print(M)
        if (i%3==0):
            current_pts.append((M.r, M.f))
            all_pts.append((M.r, M.f))
            if len(current_pts) >= MAX_PTS_SHOWN:
                current_pts.pop(0)
            print(len(current_pts))
            for pt in current_pts:
                plt.scatter(pt[0], pt[1], c='red')
        # plt.scatter(M.r, M.f, c='red')
            plt.draw()
            plt.pause(0.005)
        saving_xlim = plt.xlim()
        saving_ylim = plt.ylim()
        plt.clf() 
        plt.xlim(saving_xlim)
        plt.ylim(saving_ylim)

        M.execute_single_iteration()


        # if (i%100==0):
        #     saving_xlim = plt.xlim()
        #     saving_ylim = plt.ylim()
        #     plt.clf() 
        #     plt.xlim(saving_xlim)
        #     plt.ylim(saving_ylim)
        
    
        
    plt.show()