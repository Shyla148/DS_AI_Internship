import csv
import io

def read_csv_string(csv_data):
    """Reads a CSV-formatted string and extracts rows as dictionaries."""
    stream = io.StringIO(csv_data)
    reader = csv.DictReader(stream)
    return list(reader)

# Program execution
data_str = "Name,Age,City\nAlice,30,New York\nBob,25,London"
records = read_csv_string(data_str)
print("Parsed CSV Records:", records)