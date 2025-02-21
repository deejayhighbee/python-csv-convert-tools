import bson
import pandas as pd
import json

# Function to flatten nested dictionaries
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # Convert lists to JSON strings or handle as needed
            items.append((new_key, json.dumps(v)))
        else:
            items.append((new_key, v))
    return dict(items)

# Read BSON data from file
with open('data.bson', 'rb') as f:
    data = bson.decode_all(f.read())

# Flatten each BSON document
flattened_data = [flatten_dict(doc) for doc in data]

# Create a pandas DataFrame
df = pd.DataFrame(flattened_data)

# Export the DataFrame to CSV
df.to_csv('output.csv', index=False)

print("Conversion Complete! 'output.csv' has been created.")
