import csv

def remove_retired_rows(input_file, output_file):
    """
    Reads a CSV, skipping any rows where 'status' is 'retired'.
    Writes remaining rows to a new CSV file.
    """
    with open(input_file, 'r', encoding='utf-8', newline='') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile, delimiter=',')
        writer = csv.writer(outfile, delimiter=',')

        # Read and write header
        header = next(reader)
        writer.writerow(header)

        # Get the index of "status" column
        try:
            status_index = header.index("status")
        except ValueError:
            print("No 'status' column found in the CSV header.")
            return

        # Write only rows that do not have "retired" in the "status" column
        row_count = 0
        skipped_count = 0
        
        for row in reader:
            # Ensure row has enough columns
            if len(row) > status_index and row[status_index].strip().lower() == 'retired':
                skipped_count += 1
                continue
            writer.writerow(row)
            row_count += 1

        print(f"Wrote {row_count} rows to '{output_file}', skipped {skipped_count} retired rows.")

if __name__ == "__main__":
    # Example usage:
    input_csv = "file.csv"            # Path to your input CSV
    output_csv = "file.csv"    # Path to output CSV without "retired" rows

    remove_retired_rows(input_csv, output_csv)
