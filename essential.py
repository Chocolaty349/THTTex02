import numpy as np

def random_diagonal_dominant_mat(size:int):
    A = np.random.uniform(0,20,size=(size,size))
    for i in range(size):
        row_sum = np.sum(np.abs(A[i, :])) 
        A[i,i] = row_sum + 1.2
    return A