# Welcome to Fruit Shopping Cart

print("     WELCOME TO SHOPPING CART")

# Fruit prices
prices = {
    "apple": 100,
    "banana": 40,
    "mango": 80,
    "orange": 60,
    "grapes": 120
}

cart = []
total_items = 0
total_cost = 0

while True:
    fruit = input("\nEnter Fruit Name: ").lower()

    if fruit not in prices:
        print("Fruit not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    cost = prices[fruit] * quantity

    # Store as tuple
    cart.append((fruit, quantity, cost))

    total_items += quantity
    total_cost += cost

    choice = input("\nType 'done' to Checkout or 'add' to Continue: ").lower()

    if choice == "done":
        break

print("\n SHOPPING CART ")

print("\nFruit List:")
for item in cart:
    print(item[0])

print("\nTotal Number of Items:", total_items)

print("\nCost Details (Tuple):")
for item in cart:
    print(item)

print("\nTotal Cost = ₹", total_cost)

print("\n CHECKOUT ")
print("Items Purchased:", tuple(cart))
print("Grand Total: ₹", total_cost)
print("Thank You for Shopping!")