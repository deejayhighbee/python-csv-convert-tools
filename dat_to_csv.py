import os
import chardet
import pandas as pd

def detect_encoding(file_path, num_bytes=10000):
    """
    Detects the encoding of a file by reading up to `num_bytes` bytes.
    """
    with open(file_path, 'rb') as f:
        rawdata = f.read(num_bytes)
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    print(f"Detected encoding for {os.path.basename(file_path)}: {encoding}")
    return encoding

def convert_dat_to_csv(dat_file_path, csv_file_path, colspecs=None, column_names=None, encoding=None):
    """
    Converts a fixed-width .dat file to CSV. If no encoding is provided,
    it will attempt to detect it automatically.
    """
    if os.path.getsize(dat_file_path) == 0:
        print(f"Skipping empty file: {dat_file_path}")
        return

    # Detect encoding if not specified
    if encoding is None:
        encoding = detect_encoding(dat_file_path)

    try:
        # Let pandas infer the fixed-width fields if colspecs is not provided.
        df = pd.read_fwf(
            dat_file_path, 
            colspecs=colspecs, 
            names=column_names, 
            encoding=encoding, 
            skip_blank_lines=True,
            dtype=str,  # Read all data as strings to prevent type issues
            infer_nrows=100
        )
        
        # If no column names were provided, assign default names.
        if column_names is None:
            df.columns = [f"col{i}" for i in range(1, len(df.columns) + 1)]
        
        # Strip whitespace from string columns
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        
        df.to_csv(csv_file_path, index=False)
        print(f"Successfully converted {os.path.basename(dat_file_path)} to {os.path.basename(csv_file_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(dat_file_path)}: {e}")

def main():
    # Define the directory containing the .dat files
    dat_directory = "./dat_files"  # Adjust the path as needed
    
    # Define output directory for CSV files
    csv_directory = "./csv_output"
    os.makedirs(csv_directory, exist_ok=True)
    
    # Process every .dat file in the directory dynamically
    for filename in os.listdir(dat_directory):
        if filename.endswith(".dat"):
            file_path = os.path.join(dat_directory, filename)
            csv_filename = filename.replace(".dat", ".csv")
            csv_path = os.path.join(csv_directory, csv_filename)
            
            convert_dat_to_csv(file_path, csv_path, colspecs=None, column_names=None, encoding=None)

if __name__ == "__main__":
    main()
