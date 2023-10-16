import numpy as np

# Set the seed for reproducibility (optional)
#np.random.seed(1)

# Generate a random vector of size 5
random_vector = []
for i in range(10): #generate 10 random vector in Z^10
    vector = np.array(np.random.randint(-100,101,10))
    random_vector.append(vector)
    print(random_vector[i]) #print created vector
matrix = np.column_stack(random_vector)

matrix #print matrix 

#checking whether creted vectors are linearly independent
dim_vector = random_vector[i].shape[0]
print("Cac vector trong khong gian " + str(dim_vector) + " chieu")
if(np.linalg.matrix_rank(matrix) == matrix.shape[0]):
    print("Cac vector doc lap tuyen tinh")
else:
    print("Cac vector phu thuoc tuyen tinh")
#if rank of matrix with these vectors as its columns are equals to number of rows(dim(Z^10)) => linearly independent

