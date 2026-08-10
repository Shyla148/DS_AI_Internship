import pickle

def serialize_and_restore(data_object):
    """Serializes a Python object to bytes and restores it back."""
    serialized_bytes = pickle.dumps(data_object)
    restored_object = pickle.loads(serialized_bytes)
    return restored_object

# Program execution
original_data = {"id": 101, "items": ["apple", "banana"]}
restored_data = serialize_and_restore(original_data)
print("Restored Data:", restored_data)