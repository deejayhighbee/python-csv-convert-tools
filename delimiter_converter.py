import csv

def convert_delimited_file(input_file, output_file, input_delimiter, output_delimiter):
    """
    Converts a delimited CSV file to another delimiter format.

    Parameters:
    - input_file: Path to the input CSV file.
    - output_file: Path to the output CSV file.
    - input_delimiter: The delimiter used in the input file.
    - output_delimiter: The desired delimiter for the output file.
    """
    try:
        # Open the input file with 'utf-8-sig' to handle BOM if present
        with open(input_file, mode='r', encoding='utf-8-sig', newline='') as infile:
            reader = csv.reader(infile, delimiter=input_delimiter)
            
            # Open the output file with 'utf-8' encoding
            with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=output_delimiter, quoting=csv.QUOTE_MINIMAL)
                
                for row in reader:
                    writer.writerow(row)
        
        print(f"Successfully converted '{input_file}' to '{output_file}' using '{output_delimiter}' as the delimiter.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    input_csv = 'input.csv'    # Replace with your input file path
    output_csv = 'output.csv'  # Replace with your desired output file path
    input_delim = ';'          # The delimiter in the input file
    output_delim = ','         # The desired delimiter for the output file
    convert_delimited_file(input_csv, output_csv, input_delim, output_delim)
