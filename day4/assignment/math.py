import math

def calculate_hypotenuse(a, b):
    """Calculates the hypotenuse of a right-angled triangle given sides a and b."""
    return math.hypot(a, b)

# Program execution
side_a, side_b = 3, 4
hypotenuse = calculate_hypotenuse(side_a, side_b)
print(f"Hypotenuse for sides {side_a} and {side_b}:", hypotenuse)