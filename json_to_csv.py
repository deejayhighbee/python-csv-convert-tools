import json
import csv
import argparse
import sys
from collections import OrderedDict

def json_to_csv(json_input_path, csv_output_path):
    """
    Converts a JSON file to a CSV file with all fields treated as plain text.

    Args:
        json_input_path (str): Path to the input JSON file.
        csv_output_path (str): Path to the output CSV file.
    """
    try:
        with open(json_input_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Ensure the JSON data is a list of dictionaries
        if not isinstance(data, list):
            raise ValueError("JSON data must be a list of objects (dictionaries).")

        if not data:
            raise ValueError("JSON data is empty.")

        # Extract field names (keys) from the first dictionary
        # Use OrderedDict to preserve the order of keys
        fieldnames = list(OrderedDict.fromkeys(k for item in data for k in item.keys()))

        with open(csv_output_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writeheader()

            for entry in data:
                # Convert all values to strings to ensure they're treated as plain text
                str_entry = {key: str(value) if value is not None else "" for key, value in entry.items()}
                writer.writerow(str_entry)

        print(f"Successfully converted '{json_input_path}' to '{csv_output_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{json_input_path}' does not exist.", file=sys.stderr)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON. {e}", file=sys.stderr)
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description='Convert JSON to CSV with all fields as plain text.')
    parser.add_argument('input_json', help='Path to the input JSON file.')
    parser.add_argument('output_csv', help='Path to the output CSV file.')

    args = parser.parse_args()

    json_to_csv(args.input_json, args.output_csv)

if __name__ == "__main__":
    main()
