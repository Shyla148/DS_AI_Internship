import pandas as pd
import numpy as np

# 1. Create a Series with different cases and missing values
names = pd.Series(['Al ice', 'BOB', np.nan, 'Charlie', 'DAVID', None, 'eve'])
print("--- Original Series ---")
print(names)
# 2. Detect missing values
print("\n Missing Values")
print(names.isnull())
# 3. Fill missing values with a default placeholder
names_filled = names.fillna('Unknown')
print("\nAfter Filling Missing Values")
print(names_filled)

# 4. Convert all names to lowercase using .str operations
names_lower = names_filled.str.lower()
print("\nLowercase Names ")
print(names_lower)

# 5. Filter names containing the letter 'a'
filtered_names = names_lower[names_lower.str.contains('a')]
print("\nNames containing letter 'a'")
print(filtered_names)

#6.starts with 'a'
names_start_a = names_lower[names_lower.str.startswith('a')]
print("\nNames starting with letter 'a'")
print(names_start_a)


names_end_e = names_lower[names_lower.str.endswith('e')]
print("\nNames ending with letter 'e'")
print(names_end_e)

#replace 'a' with '@'
names_replaced = names_lower.str.replace('a', '@')
print("\nNames after replacing 'a' with '@'")
print(names_replaced)

#strip whitespace from names
names_stripped = names.str.strip()
print("\nNames after stripping whitespace")
print(names_stripped)