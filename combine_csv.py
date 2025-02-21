import os
import glob

def combine_csv_files(folder_path, output_file):
    """
    Combines all CSV files in the specified folder into a single CSV file without altering encoding.

    Parameters:
    - folder_path: Path to the folder containing CSV files.
    - output_file: Path for the combined output CSV file.
    """
    # Get a sorted list of all CSV files in the folder
    csv_files = sorted(glob.glob(os.path.join(folder_path, '*.csv')))
    
    if not csv_files:
        print("No CSV files found in the specified folder.")
        return
    
    try:
        with open(output_file, 'wb') as outfile:
            for i, fname in enumerate(csv_files):
                with open(fname, 'rb') as infile:
                    lines = infile.readlines()
                    if not lines:
                        print(f"Skipping empty file: {fname}")
                        continue  # Skip empty files
                    
                    if i == 0:
                        # Write all lines from the first file, including header
                        outfile.writelines(lines)
                        print(f"Writing header and data from {fname}")
                    else:
                        # Write all lines except the first (header)
                        outfile.writelines(lines[1:])
                        print(f"Writing data from {fname} (header skipped)")
        print(f"Successfully combined {len(csv_files)} files into {output_file}")
    except Exception as e:
        print(f"Error during file combination: {e}")

if __name__ == "__main__":
    # Define the folder containing CSV files
    folder = 'main'  # Ensure this folder exists in the current directory
    
    # Define the output file path
    output = os.path.join(folder, 'combined.csv')
    
    # Call the function to combine CSV files
    combine_csv_files(folder, output)
