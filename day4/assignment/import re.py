import re

def extract_phone_numbers(text):
    """Extracts 10-digit telephone numbers from a given string."""
    pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
    return re.findall(pattern, text)

# Program execution
sample_text = "Call support at 555-123-4567 or emergency at 555.987.6543."
numbers = extract_phone_numbers(sample_text)
print("Found Phone Numbers:", numbers)