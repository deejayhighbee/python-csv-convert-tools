# Python .csv convert tools

**bson-to-csv**
This script performs a complete data conversion process:

Imports and Setup:
It imports necessary libraries:

bson for decoding BSON files.
pandas for data manipulation and creating a DataFrame.
json for handling list-to-string conversion.
Flattening Nested Dictionaries:
The flatten_dict function takes a nested dictionary and converts it into a flat dictionary.

It concatenates keys from nested dictionaries using a period (.) as a separator.
If a value is a list, it converts it into a JSON string.
This ensures that even deeply nested structures become a single-level dictionary suitable for tabular representation.
Reading BSON Data:
The script opens a file named data.bson in binary mode and uses bson.decode_all to read and decode all BSON documents into Python dictionaries.

Processing and Creating DataFrame:
Each BSON document is flattened using the flatten_dict function.
The list of these flattened dictionaries is then converted into a pandas DataFrame, which organizes the data into rows and columns.

Exporting to CSV:
Finally, the DataFrame is exported to a CSV file named output.csv, and a confirmation message is printed.
