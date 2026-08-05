# Create an empty list
numbers = []

# Take input from the user
n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Display the list
print("\nList:", numbers)

# Print results
print("Minimum Value:", min(numbers))
print("Maximum Value:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Total Length:", len(numbers))
print("Sorted List:", sorted(numbers))