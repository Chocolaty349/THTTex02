import numpy as np

random_square_mat = np.random.randint(0,100,size=(5,5))
randon_matrix_1 = np.random.randint(0,100,size=(5,4))
randon_matrix_2 = np.random.randint(0,100,size=(5,4))

print("Tong hai ma tran:")
print(randon_matrix_1 + randon_matrix_2)

print("Tich hai ma tran:")
print(randon_matrix_1.T @ randon_matrix_2)

print("Chuyen vi lan luot cua ma tran 1 va 2:")
print(randon_matrix_1.T)
print(randon_matrix_2.T)

print("Nghich dao cua ma tran vuong:")
print(np.linalg.inv(random_square_mat))

print("Gia tri rieng va vector rieng cua ma tran vuong:")
print(np.linalg.eig(random_square_mat))



