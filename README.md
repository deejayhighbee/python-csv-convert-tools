# Python CSV Convert Tools

This repository provides a collection of Python scripts designed to convert and manipulate various file formats (BSON, CSV, DAT, JSON, etc.) into CSV. Each script has a specific purpose, and the descriptions below outline their functionality and usage.

---

## [Convert BSON to CSV](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/bson_convert.py)

This script performs a complete data conversion process from BSON to CSV.

### Key Steps

- **Imports and Setup:**
  - Imports necessary libraries:
    - `bson` for decoding BSON files.
    - `pandas` for data manipulation and creating DataFrames.
    - `json` for handling list-to-string conversions.
  
- **Flattening Nested Dictionaries:**
  - Uses the `flatten_dict` function to convert nested dictionaries into a single-level dictionary.
  - Concatenates keys from nested dictionaries using a period (`.`) as a separator.
  - Converts list values into JSON strings.

- **Reading BSON Data:**
  - Opens `data.bson` in binary mode.
  - Uses `bson.decode_all` to decode all BSON documents into Python dictionaries.

- **Processing and Creating DataFrame:**
  - Flattens each BSON document with the `flatten_dict` function.
  - Converts the list of flattened dictionaries into a pandas DataFrame.

- **Exporting to CSV:**
  - Exports the DataFrame to `output.csv`.
  - Prints a confirmation message upon successful export.

---

## [Combine CSV Files](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/combine_csv.py)

This script combines multiple CSV files from a specified folder into a single CSV file while preserving their original encoding.

### Functionality Breakdown

1. **Gathering CSV Files:**
   - Uses the `glob` module to locate all `.csv` files within the given folder.
   - Sorts the list of files to maintain a consistent order.

2. **File Combination Process:**
   - Opens the output file in binary write mode (`'wb'`) to preserve encoding.
   - **First File:**
     - Reads all lines (including the header) and writes them to the output.
   - **Subsequent Files:**
     - Reads each file but skips the header to avoid duplicate headers.
   - Skips any empty files, printing a message when encountered.

3. **Error Handling and Completion Message:**
   - Wraps the process in a try-except block to catch and report errors.
   - Prints a confirmation message that includes the number of files combined and the output file path upon success.

4. **Script Execution:**
   - When executed as the main module, defines a folder (e.g., `main`) and an output file path (`combined.csv`), then calls the function to combine the files.

---

## [Convert .dat to .csv](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/dat_to_csv.py)

This utility converts fixed-width `.dat` files into CSV format.

### Detailed Steps

1. **Encoding Detection:**
   - **Function:** `detect_encoding`
   - Opens a file in binary mode and reads up to 10,000 bytes.
   - Uses the `chardet` library to guess the file’s encoding.
   - Prints and returns the detected encoding.

2. **Conversion Process:**
   - **Function:** `convert_dat_to_csv`
   - **Checks:**
     - Skips conversion if the `.dat` file is empty, printing a message.
     - If no encoding is provided, uses `detect_encoding` to determine the file's encoding.
   - **Reading Data:**
     - Uses `pandas.read_fwf` to read fixed-width formatted data.
     - Accepts optional parameters for column specifications (`colspecs`) and column names.
     - Reads all data as strings (to avoid type conversion issues) and skips blank lines.
   - **Post-Processing:**
     - Assigns default column names (e.g., `col1`, `col2`, etc.) if none are provided.
     - Strips extra whitespace from the data.
   - **Output:**
     - Writes the processed DataFrame to a CSV file without including the index.
     - Prints a success message upon completion.

3. **Processing Multiple Files:**
   - **Function:** `main`
   - Defines an input directory (e.g., `./dat_files`) containing `.dat` files.
   - Creates an output directory (e.g., `./csv_output`) if it does not exist.
   - Iterates over every `.dat` file, constructs the corresponding CSV filename, and calls `convert_dat_to_csv`.

4. **Script Execution:**
   - Runs as a standalone program to automatically process all `.dat` files in the specified folder and generate CSV files in the output directory.

---

## [Delete Rows Where](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/delete_rows_where.py)

This script processes a CSV file by creating a new CSV that excludes rows where the `status` column is set to `"retired"`.

### How It Works

- **File Opening:**
  - Opens the input CSV for reading and the output CSV for writing using UTF-8 encoding.
  - Handles files with proper newline settings.

- **Header Processing:**
  - Reads and writes the header row.
  - Searches for the `status` column; if not found, prints a message and exits.

- **Row Filtering:**
  - Iterates through each row, checking the value in the `status` column (ignoring case and trimming whitespace).
  - Skips rows where the value is `"retired"` and writes all other rows to the output.
  - Keeps count of rows written versus rows skipped.

- **Completion Message:**
  - Prints a summary indicating the number of rows written and the number skipped after processing all rows.

- **Usage Example:**
  - The `if __name__ == "__main__":` block demonstrates how to call the `remove_retired_rows` function with specified input and output file paths.

---

## [Delimiter Converter](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/delimiter_converter.py)

This script converts a CSV file’s delimiters.

### Key Features

1. **Input and Output Handling:**
   - Opens the input CSV with `'utf-8-sig'` encoding to handle any BOM.
   - Opens the output CSV with `'utf-8'` encoding.

2. **Reading and Writing CSV Data:**
   - Uses `csv.reader` to parse the input file with a specified delimiter.
   - Uses `csv.writer` to write each row to the output file with a new delimiter.
   - Configures the writer with `quoting=csv.QUOTE_MINIMAL` to quote fields only when necessary.

3. **Error Handling:**
   - Implements a try-except block to manage errors such as `FileNotFoundError` or other exceptions.

4. **Example Usage:**
   - When executed as the main program, calls `convert_delimited_file` with sample file paths and delimiters (e.g., converting a semicolon-separated file to a comma-separated file).

---

## [Detect Character Encoding](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/encode.py)

This script uses the `chardet` library to detect the character encoding of a given file.

### Breakdown

1. **Reading File Data:**
   - The `detect_encoding` function opens the file in binary mode (`'rb'`).
   - Reads a specified number of bytes (default is 10,000) for analysis.

2. **Detecting the Encoding:**
   - Passes the raw byte data to `chardet.detect()`, which returns encoding details.
   - Extracts and returns the value of the `encoding` key.

3. **Usage:**
   - The main block calls `detect_encoding` on a file (e.g., `file.csv`) and prints the detected encoding.

---

## [Convert JSON to CSV](https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/json_to_csv.py)

This script converts a JSON file into a CSV file while ensuring that all fields are treated as plain text.

### Detailed Process

1. **JSON Parsing:**
   - Opens and reads the specified JSON file.
   - Expects the JSON data to be a list of dictionaries; raises a `ValueError` if the data is not as expected or is empty.

2. **Extracting Field Names:**
   - Uses an `OrderedDict` to extract and preserve the order of keys from the JSON dictionaries.
   - These keys become the column headers for the CSV.

3. **CSV Writing:**
   - Opens the output CSV file for writing.
   - Uses `csv.DictWriter` with `quoting=csv.QUOTE_ALL` so that every field is quoted.
   - Converts each dictionary’s values to strings (or empty strings for `None`) before writing.

4. **Error Handling:**
   - Incorporates multiple error checks for file not found errors, JSON decoding issues, and other exceptions with informative messages.

5. **Command-Line Interface:**
   - Uses the `argparse` module to allow running the script from the command line.
   - Requires two positional arguments: the input JSON file path and the output CSV file path.
   - **Example Usage:**
     ```bash
     python json_to_csv.py input.json output.csv
     ```
   - Adjust the command to use `python3` if necessary.

---
