import json

def parse_and_format_json(json_string):
    """Parses a raw JSON string into a Python dictionary and formats it back."""
    data = json.loads(json_string)
    data["processed"] = True
    return json.dumps(data, indent=2)

# Program execution
raw_json = '{"name": "Alice", "role": "Developer"}'
formatted_json = parse_and_format_json(raw_json)
print("Updated JSON:\n", formatted_json)