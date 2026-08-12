import numpy as np

sales = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40],
    [25, 35, 45]
])

print("Sales Data:")
print(sales)

# Product-wise: axis=0    10 15 20 25 
print("\nProduct-wise Mean:", np.mean(sales, axis=0))
print("Product-wise Median:", np.median(sales, axis=0))
print("Product-wise Variance:", np.var(sales, axis=0))
print("Product-wise Standard Deviation:", np.std(sales, axis=0))

# Day-wise: axis=1 10,20,30  15,25,35  20,30,40  25,35,45
print("\nDay-wise Mean:", np.mean(sales, axis=1))
print("Day-wise Median:", np.median(sales, axis=1))
print("Day-wise Variance:", np.var(sales, axis=1))
print("Day-wise Standard Deviation:", np.std(sales, axis=1))