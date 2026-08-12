import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Matrix multiplication
print("A dot B:")
print(np.dot(A, B))
print("Shape:", np.dot(A, B).shape)

# Swap matrices
print("\nB dot A:")
print(np.dot(B, A))
print("Shape:", np.dot(B, A).shape)

# Element-wise multiplication
C = np.array([[1, 2],
              [3, 4]])

D = np.array([[5, 6],
              [7, 8]])

print("\nElement-wise C * D:")
print(C * D)