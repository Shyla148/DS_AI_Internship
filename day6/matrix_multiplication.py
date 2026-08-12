import numpy as np 
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.dot(A,B))#multiplication of two matrices using dot function

print(np.matmul(A,B))#multiplication of two matrices using matmul function

result=A@B #multiplication of two matrices using @ operator
print(result)

