import numpy as np
from essential import random_diagonal_dominant_mat

#giai he phuong trinh Ax=b bang phuong phap Jacobi
ITERATION_LIMIT = 1000


A = random_diagonal_dominant_mat(4)
print("Input matrix: ")
print(A)

b = np.random.uniform(0,20,size=4)
print("Input vector:", b)

x = np.zeros_like(b) #khoi tao x buoc thu i
x_new = np.zeros_like(x)
for iter_count in range(ITERATION_LIMIT):
    if iter_count != 0:
        print(f"Iteration {iter_count}: {x}")
    #x_new = np.zeros_like(x) #x o buoc lap tiep theo
    #x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        be4_x_i = np.dot(A[i, :i], x[:i])
        after_x_i = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - be4_x_i - after_x_i) / A[i, i]
        # if x_new[i] == x_new[i-1]:
        #   break
    if np.allclose(x, x_new, atol=1e-6, rtol=0.):#sai so nho hon 10^-6 => chap nhan nghiem
        break
    x = x_new

print("Nghiem: ")
print(x)
print("Sai so:")
print(np.dot(A, x) - b)