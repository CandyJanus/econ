import nashpy as nash
import numpy as np
A = np.array([[3, 0], [5, 1]])
B = np.array([[3, 5], [0, 1]])
prisoners_dilemma = nash.Game(A, B)
sigma_A = np.array([1 / 2, 1 / 2])
sigma_B = np.array([1 / 2, 1 / 2])
x=prisoners_dilemma[sigma_A, sigma_B]
print(x)

C = np.array([[3, 0], [5, 1]])
D = np.array([[3, 5], [0, 1]])
prisoners_dilemma = nash.Game(A, B)
sigma_C = np.array([1, 0])
sigma_D = np.array([0, 1])
x=prisoners_dilemma[sigma_C, sigma_D]
print(x)