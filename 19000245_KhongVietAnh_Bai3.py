import numpy as np

#giai he phuong trinh Ax=b bang phan ra QR 
b = np.random.randint(0,100,5)
print("Input vector:\n ", b)
A = np.random.randint(0,100,size=(5,5)) #ma tran A co 5x5
print("Input matrix:\n", A)
#phan ra QR day du ma tran vuong A
Q, R = np.linalg.qr(A, 'complete')

print("Q matrix:\n ", Q)
print("R matrix:\n ", R)
y = Q.T @ b
#sai so cho phep
allowed_tolerance_e6 = 1e-6
allowed_tolerance_e4 = 1e-4
zero = np.full(5,0)

x = np.linalg.inv(R) @ y #nghiem
epsilon = Q@R@x - b # sai so khi thay nghiem lai vao phuong trinh
print("Nghiem ", x) 

if np.allclose(epsilon, zero, atol=allowed_tolerance_e6, rtol=0.):
    print("du tot voi sai so 10^-6")
else:
    print("khong du tot voi sai so 10^-6")

if np.allclose(epsilon, zero, atol=allowed_tolerance_e4, rtol=0.):
    print("du tot voi sai so 10^-4")
else:
    print("khong du tot voi sai so 10^-4")