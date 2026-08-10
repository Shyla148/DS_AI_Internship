import itertools

def generate_combinations(items, group_size=2):
    """Generates all unique combinations of a given size from an item list."""
    return list(itertools.combinations(items, group_size))

# Program execution
letters = ["A", "B", "C", "D"]
combinations = generate_combinations(letters, 2)
print("Unique Pairs:", combinations)