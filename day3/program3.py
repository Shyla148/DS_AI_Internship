# Function to print table
def table(n):
    print("\nMultiplication Table of", n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

# Main Program
num = int(input("Enter a number: "))
table(num)