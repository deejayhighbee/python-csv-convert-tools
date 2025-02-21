<a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/bson_convert.py"><strong>Convert bson to csv</strong></a>

This script performs a complete data conversion process:

<strong>Imports and Setup: It imports necessary libraries:</strong>

bson for decoding BSON files. 

pandas for data manipulation and creating a DataFrame. 

json for handling list-to-string conversion.

<strong>Flattening Nested Dictionaries:</strong>

The flatten_dict function takes a nested dictionary and converts it into a flat dictionary. It concatenates keys from nested dictionaries using a period (.) as a separator. If a value is a list, it converts it into a JSON string. This ensures that even deeply nested structures become a single-level dictionary suitable for tabular representation.

<strong>Reading BSON Data:</strong>

The script opens a file named data.bson in binary mode and uses bson.decode_all to read and decode all BSON documents into Python dictionaries.

<strong>Processing and Creating DataFrame:</strong>

Each BSON document is flattened using the flatten_dict function. The list of these flattened dictionaries is then converted into a pandas DataFrame, which organizes the data into rows and columns.

<strong>Exporting to CSV:</strong>

Finally, the DataFrame is exported to a CSV file named output.csv, and a confirmation message is printed.

<strong>………………………………………………………………………………………………………………</strong>

<a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/combine_csv.py"><strong>Combine csv files</strong></a>

This script combines multiple CSV files from a specified folder into a single CSV file while preserving their original encoding. Here’s a breakdown of its functionality:
<ol>
 	<li><strong>Gathering CSV Files:</strong>
<ul>
 	<li>It uses the glob module to find all files ending in .csv within the given folder.</li>
 	<li>The list of files is sorted to maintain a consistent order.</li>
</ul>
</li>
 	<li><strong>File Combination Process:</strong>
<ul>
 	<li>The script opens the output file in binary write mode ('wb') to ensure the encoding remains unchanged.</li>
 	<li>It then iterates over each CSV file:
<ul>
 	<li><strong>First File:</strong>
<ul>
 	<li>Reads all lines (including the header) and writes them to the output file.</li>
</ul>
</li>
 	<li><strong>Subsequent Files:</strong>
<ul>
 	<li>Reads all lines but skips the first line (the header) to avoid duplicating headers in the combined file.</li>
</ul>
</li>
 	<li>It also skips any empty files and prints a message if encountered.</li>
</ul>
</li>
</ul>
</li>
 	<li><strong>Error Handling and Completion Message:</strong>
<ul>
 	<li>The process is wrapped in a try-except block to catch and report any errors during the file reading or writing process.</li>
 	<li>Upon successful combination, it prints a confirmation message including the number of files combined and the output file path.</li>
</ul>
</li>
 	<li><strong>Script Execution:</strong>
<ul>
 	<li>When run as the main module, it defines a folder (here, 'main') and an output file path within that folder (combined.csv), and then calls the function to perform the combination.</li>
</ul>
</li>
</ol>
In summary, the code reads all CSV files in the folder, concatenates their data into a single CSV file while ensuring only one header row is included, and maintains the original file encoding.

<strong>…………………………………………………………………………………………………………………</strong>

<a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/dat_to_csv.py"><strong>Convert .dat to .csv</strong></a>

This script is a utility for converting fixed-width .dat files into CSV format. Here's a detailed breakdown:
<ol>
 	<li><strong>Encoding Detection:</strong>
<ul>
 	<li><strong>Function:</strong> detect_encoding</li>
 	<li><strong>How it works:</strong>
<ul>
 	<li>Opens a file in binary mode and reads up to 10,000 bytes.</li>
 	<li>Uses the chardet library to guess the file's encoding.</li>
 	<li>Prints and returns the detected encoding.</li>
</ul>
</li>
</ul>
</li>
 	<li><strong>Conversion from .dat to CSV:</strong>
<ul>
 	<li><strong>Function:</strong> convert_dat_to_csv</li>
 	<li><strong>Process:</strong>
<ul>
 	<li><strong>Empty File Check:</strong> If the .dat file is empty, it prints a message and skips conversion.</li>
 	<li><strong>Encoding:</strong> If no encoding is provided, it uses detect_encoding to determine the file's encoding.</li>
 	<li><strong>Reading Data:</strong>
<ul>
 	<li>Uses pandas.read_fwf to read the fixed-width formatted data.</li>
 	<li>Allows optional parameters for column specifications (colspecs) and column names. If these aren’t provided, it lets pandas infer the structure.</li>
 	<li>Reads all data as strings (to avoid type conversion issues) and skips blank lines.</li>
</ul>
</li>
 	<li><strong>Post-Processing:</strong>
<ul>
 	<li>If no column names are given, it assigns default names like col1, col2, etc.</li>
 	<li>Strips any extra whitespace from the data.</li>
</ul>
</li>
 	<li><strong>Output:</strong>
<ul>
 	<li>Writes the processed DataFrame to a CSV file without including the index.</li>
 	<li>Prints a success message upon completion.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
 	<li><strong>Processing Multiple Files:</strong>
<ul>
 	<li><strong>Function:</strong> main</li>
 	<li><strong>Workflow:</strong>
<ul>
 	<li>Defines a directory (./dat_files) where the .dat files are located.</li>
 	<li>Creates an output directory (./csv_output) if it doesn’t already exist.</li>
 	<li>Iterates through every file in the input directory, and for each file ending with .dat:
<ul>
 	<li>Constructs the appropriate CSV output filename.</li>
 	<li>Calls convert_dat_to_csv to perform the conversion.</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
 	<li><strong>Script Execution:</strong>
<ul>
 	<li>The script is designed to run as a standalone program. When executed, it automatically processes all .dat files found in the specified folder and generates corresponding CSV files in the output directory.</li>
</ul>
</li>
</ol>
<strong>………………………………………………………………………………………………………………</strong>

<a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/delete_rows_where.py"><strong>Delete rows where</strong></a>

This script processes a CSV file by reading its contents and writing a new CSV file that excludes any rows where the "status" column is set to "retired." Here’s a detailed explanation:
<ul>
 	<li data-start="188" data-end="400"><strong data-start="188" data-end="205">File Opening:</strong><br data-start="205" data-end="208" />The script opens the input CSV file for reading and the output CSV file for writing using UTF-8 encoding. It handles files in binary mode with proper newline settings to maintain formatting.</li>
 	<li data-start="404" data-end="428"><strong data-start="404" data-end="426">Header Processing:</strong></li>
</ul>
<ul data-start="431" data-end="663">
 	<li style="list-style-type: none;">
<ul>
 	<li data-start="431" data-end="522">It reads the first line as the header and writes this header directly to the output file.</li>
 	<li data-start="525" data-end="663">It then searches for the "status" column in the header. If the "status" column is not found, it prints a message and exits the function.</li>
</ul>
</li>
</ul>
<ul>
 	<li data-start="667" data-end="687"><strong data-start="667" data-end="685">Row Filtering:</strong></li>
</ul>
<ul data-start="690" data-end="1017">
 	<li style="list-style-type: none;">
<ul>
 	<li data-start="690" data-end="740">The script iterates through each row in the CSV.</li>
 	<li data-start="743" data-end="842">For each row, it checks the value in the "status" column (ignoring case and trimming whitespace).</li>
 	<li data-start="845" data-end="943">If the value is "retired," the row is skipped; otherwise, the row is written to the output file.</li>
 	<li data-start="946" data-end="1017">It keeps count of how many rows are written and how many are skipped.</li>
</ul>
</li>
</ul>
<ul>
 	<li data-start="1021" data-end="1217"><strong data-start="1021" data-end="1044">Completion Message:</strong><br data-start="1044" data-end="1047" />After processing all rows, the script prints a summary stating how many rows were written to the output file and how many rows were skipped due to the "retired" status.</li>
 	<li data-start="1221" data-end="1390"><strong data-start="1221" data-end="1239">Usage Example:</strong><br data-start="1239" data-end="1242" />The if __name__ == "__main__": block demonstrates how to call the remove_retired_rows function with specified input and output CSV file paths.</li>
</ul>
&nbsp;
<strong>………………………………………………………………………………………………………………</strong>
&nbsp;
<p data-start="0" data-end="191"><a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/delimiter_converter.py">Delimiter converter</a></p>

&nbsp;
<p data-start="0" data-end="191">This Python script defines a function, <strong data-start="39" data-end="65">convert_delimited_file</strong>, that reads a CSV file using one delimiter and writes it out using a different delimiter. Here's a breakdown of what it does:</p>

<ol>
 	<li style="list-style-type: none;">
<ol data-start="193" data-end="1276">
 	<li data-start="193" data-end="453">
<p data-start="196" data-end="228"><strong data-start="196" data-end="226">Input and Output Handling:</strong></p>

<ul data-start="232" data-end="453">
 	<li data-start="232" data-end="394">It opens the input CSV file with <code data-start="267" data-end="280">'utf-8-sig'</code> encoding. This encoding is useful for handling files that might include a Byte Order Mark (BOM) at the beginning.</li>
 	<li data-start="398" data-end="453">It opens the output CSV file with <code data-start="434" data-end="443">'utf-8'</code> encoding.</li>
</ul>
</li>
 	<li data-start="455" data-end="822">
<p data-start="458" data-end="493"><strong data-start="458" data-end="491">Reading and Writing CSV Data:</strong></p>

<ul data-start="497" data-end="822">
 	<li data-start="497" data-end="600">The function uses Python's <code data-start="526" data-end="538">csv.reader</code> to read the input file using the specified <code data-start="582" data-end="599">input_delimiter</code>.</li>
 	<li data-start="604" data-end="708">It then uses <code data-start="619" data-end="631">csv.writer</code> to write each row to the output file using the specified <code data-start="689" data-end="707">output_delimiter</code>.</li>
 	<li data-start="712" data-end="822">The writer is configured with <code data-start="744" data-end="771">quoting=csv.QUOTE_MINIMAL</code>, meaning it will only quote fields when necessary.</li>
</ul>
</li>
 	<li data-start="824" data-end="993">
<p data-start="827" data-end="848"><strong data-start="827" data-end="846">Error Handling:</strong></p>

<ul data-start="852" data-end="993">
 	<li data-start="852" data-end="993">The function includes a <code data-start="878" data-end="890">try-except</code> block to catch errors like a missing input file (<code data-start="940" data-end="959">FileNotFoundError</code>) or any other general exceptions.</li>
</ul>
</li>
 	<li data-start="995" data-end="1276">
<p data-start="998" data-end="1018"><strong data-start="998" data-end="1016">Example Usage:</strong></p>

<ul data-start="1022" data-end="1276">
 	<li data-start="1022" data-end="1276">When the script is run as the main program, it calls the <code data-start="1081" data-end="1105">convert_delimited_file</code> function with sample file paths and delimiters (e.g., converting a file where values are separated by semicolons (<code data-start="1220" data-end="1223">;</code>) to one where values are separated by commas (<code data-start="1270" data-end="1273">,</code>)).</li>
</ul>
</li>
</ol>
</li>
</ol>
