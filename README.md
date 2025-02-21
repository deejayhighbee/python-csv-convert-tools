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
………………………………………………………………………………………………………………
**Combine CSV File**

This script combines multiple CSV files from a specified folder into a single CSV file while preserving their original encoding. Here’s a breakdown of its functionality:
1.	Gathering CSV Files:
o	It uses the glob module to find all files ending in .csv within the given folder.
o	The list of files is sorted to maintain a consistent order.
2.	File Combination Process:
o	The script opens the output file in binary write mode ('wb') to ensure the encoding remains unchanged.
o	It then iterates over each CSV file:
	First File:
	Reads all lines (including the header) and writes them to the output file.
	Subsequent Files:
	Reads all lines but skips the first line (the header) to avoid duplicating headers in the combined file.
	It also skips any empty files and prints a message if encountered.
3.	Error Handling and Completion Message:
o	The process is wrapped in a try-except block to catch and report any errors during the file reading or writing process.
o	Upon successful combination, it prints a confirmation message including the number of files combined and the output file path.
4.	Script Execution:
o	When run as the main module, it defines a folder (here, 'main') and an output file path within that folder (combined.csv), and then calls the function to perform the combination.
In summary, the code reads all CSV files in the folder, concatenates their data into a single CSV file while ensuring only one header row is included, and maintains the original file encoding.

…………………………………………………………………………………………………………………
**Convert .dat to .csv**

This script is a utility for converting fixed-width .dat files into CSV format. Here's a detailed breakdown:
1.	Encoding Detection:
o	Function: detect_encoding
o	How it works:
	Opens a file in binary mode and reads up to 10,000 bytes.
	Uses the chardet library to guess the file's encoding.
	Prints and returns the detected encoding.
2.	Conversion from .dat to CSV:
o	Function: convert_dat_to_csv
o	Process:
	Empty File Check: If the .dat file is empty, it prints a message and skips conversion.
	Encoding: If no encoding is provided, it uses detect_encoding to determine the file's encoding.
	Reading Data:
	Uses pandas.read_fwf to read the fixed-width formatted data.
	Allows optional parameters for column specifications (colspecs) and column names. If these aren’t provided, it lets pandas infer the structure.
	Reads all data as strings (to avoid type conversion issues) and skips blank lines.
	Post-Processing:
	If no column names are given, it assigns default names like col1, col2, etc.
	Strips any extra whitespace from the data.
	Output:
	Writes the processed DataFrame to a CSV file without including the index.
	Prints a success message upon completion.
3.	Processing Multiple Files:
o	Function: main
o	Workflow:
	Defines a directory (./dat_files) where the .dat files are located.
	Creates an output directory (./csv_output) if it doesn’t already exist.
	Iterates through every file in the input directory, and for each file ending with .dat:
	Constructs the appropriate CSV output filename.
	Calls convert_dat_to_csv to perform the conversion.
4.	Script Execution:
o	The script is designed to run as a standalone program. When executed, it automatically processes all .dat files found in the specified folder and generates corresponding CSV files in the output directory.
………………………………………………………………………………………………………………

**Delete rows where**

This script processes a CSV file by reading its contents and writing a new CSV file that excludes any rows where the "status" column is set to "retired." Here’s a detailed explanation:
•	File Opening:
The script opens the input CSV file for reading and the output CSV file for writing using UTF-8 encoding. It handles files in binary mode with proper newline settings to maintain formatting.
•	Header Processing:
o	It reads the first line as the header and writes this header directly to the output file.
o	It then searches for the "status" column in the header. If the "status" column is not found, it prints a message and exits the function.
•	Row Filtering:
o	The script iterates through each row in the CSV.
o	For each row, it checks the value in the "status" column (ignoring case and trimming whitespace).
o	If the value is "retired," the row is skipped; otherwise, the row is written to the output file.
o	It keeps count of how many rows are written and how many are skipped.
•	Completion Message:
After processing all rows, the script prints a summary stating how many rows were written to the output file and how many rows were skipped due to the "retired" status.
•	Usage Example:
The if __name__ == "__main__": block demonstrates how to call the remove_retired_rows function with specified input and output CSV file paths.

