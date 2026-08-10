import random

def generate_random_passcode(length=6):
    """Generates a random numeric passcode of specified length."""
    digits = [str(random.randint(0, 9)) for _ in range(length)]
    return "".join(digits)

# Program execution
passcode = generate_random_passcode()
print("Generated Passcode:", passcode)