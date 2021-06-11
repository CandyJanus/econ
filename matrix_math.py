import numpy as np
import pandas as pd
import quantecon as qe

#figuring out basic matrix math again

x=np.array([[-1, -10],[0,-9]])
 
m1=pd.DataFrame(x, columns=['dove', 'hawk'])
m1.index = ['dove', 'hawk']
m2=m1.T

pt = [[(-1,-1), (-10,0)], [(0,-10), (-9,-9)]]
g = qe.game_theory.NormalFormGame(pt)
print(g)

