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


&nbsp;
<strong>………………………………………………………………………………………………………………</strong>
&nbsp;

<p data-start="0" data-end="117"><a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/encode.py"><strong>Detect character encoding</strong></a></p>
<p data-start="0" data-end="117">This Python script uses the <strong data-start="28" data-end="39">chardet</strong> library to detect the character encoding of a given file. Here’s a breakdown:</p>

<ol data-start="119" data-end="758">
 	<li data-start="119" data-end="342">
<p data-start="122" data-end="146"><strong data-start="122" data-end="144">Reading File Data:</strong></p>

<ul data-start="150" data-end="342">
 	<li data-start="150" data-end="222">The function <code data-start="165" data-end="182">detect_encoding</code> opens the file in binary mode (<code data-start="214" data-end="220">'rb'</code>).</li>
 	<li data-start="226" data-end="342">It reads a specified number of bytes (default is 10,000) from the file. This sample is used to guess the encoding.</li>
</ul>
</li>
 	<li data-start="344" data-end="606">
<p data-start="347" data-end="376"><strong data-start="347" data-end="374">Detecting the Encoding:</strong></p>

<ul data-start="380" data-end="606">
 	<li data-start="380" data-end="514">The raw byte data is passed to <code data-start="413" data-end="431">chardet.detect()</code>, which analyzes it and returns a dictionary containing details about the encoding.</li>
 	<li data-start="518" data-end="606">The function then extracts and returns the value associated with the <code data-start="589" data-end="601">'encoding'</code> key.</li>
</ul>
</li>
 	<li data-start="608" data-end="758">
<p data-start="611" data-end="623"><strong data-start="611" data-end="621">Usage:</strong></p>

<ul data-start="627" data-end="758">
 	<li data-start="627" data-end="715">In the main block, the script calls <code data-start="665" data-end="682">detect_encoding</code> on a file named <code data-start="699" data-end="714">'file.csv'</code>.</li>
 	<li data-start="719" data-end="758">It then prints the detected encoding.</li>
</ul>
</li>
</ol>
</li>
</ol>
</li>
</ol>
<p data-start="0" data-end="167"></p>
&nbsp;
<strong>………………………………………………………………………………………………………………</strong>
&nbsp;


<p data-start="0" data-end="167"><a href="https://github.com/deejayhighbee/python-csv-convert-tools/blob/main/json_to_csv.py"><strong>Convert .json to .csv</strong></a></p>
<p data-start="0" data-end="167">This Python script converts a JSON file into a CSV file while ensuring that all fields are treated as plain text. Here's a step-by-step breakdown of its functionality:</p>

<ol data-start="169" data-end="1453">
 	<li data-start="169" data-end="378">
<p data-start="172" data-end="191"><strong data-start="172" data-end="189">JSON Parsing:</strong></p>

<ul data-start="195" data-end="378">
 	<li data-start="195" data-end="248">The script opens and reads the specified JSON file.</li>
 	<li data-start="252" data-end="378">It expects the JSON data to be a list of dictionaries. If it isn't, or if the list is empty, the script raises a ValueError.</li>
</ul>
</li>
 	<li data-start="380" data-end="592">
<p data-start="383" data-end="412"><strong data-start="383" data-end="410">Extracting Field Names:</strong></p>

<ul data-start="416" data-end="592">
 	<li data-start="416" data-end="519">It uses an <code data-start="429" data-end="442">OrderedDict</code> to extract and preserve the order of keys from all dictionaries in the list.</li>
 	<li data-start="523" data-end="592">These keys become the column headers (fieldnames) for the CSV file.</li>
</ul>
</li>
 	<li data-start="594" data-end="935">
<p data-start="597" data-end="615"><strong data-start="597" data-end="613">CSV Writing:</strong></p>

<ul data-start="619" data-end="935">
 	<li data-start="619" data-end="670">The script opens the output CSV file for writing.</li>
 	<li data-start="674" data-end="792">It uses <code data-start="684" data-end="700">csv.DictWriter</code> with the <code data-start="710" data-end="733">quoting=csv.QUOTE_ALL</code> option, which means every field in the CSV will be quoted.</li>
 	<li data-start="796" data-end="935">Each value in the dictionaries is converted to a string (or set to an empty string if the value is <code data-start="897" data-end="903">None</code>) before being written as a row.</li>
</ul>
</li>
 	<li data-start="937" data-end="1134">
<p data-start="940" data-end="961"><strong data-start="940" data-end="959">Error Handling:</strong></p>

<ul data-start="965" data-end="1134">
 	<li data-start="965" data-end="1134">The script includes multiple error checks to handle file not found errors, JSON decoding issues, and other unexpected exceptions, providing informative error messages.</li>
</ul>
</li>
 	<li data-start="1136" data-end="1453">
<p data-start="1139" data-end="1168"><strong data-start="1139" data-end="1166">Command-Line Interface:</strong></p>

<ul data-start="1172" data-end="1453">
 	<li data-start="1172" data-end="1365">The script uses the <code data-start="1194" data-end="1204">argparse</code> module to allow users to run it from the command line, requiring two positional arguments: the path to the input JSON file and the path for the output CSV file.</li>
 	<li data-start="1369" data-end="1453">When executed directly, it parses the arguments and calls the conversion function.</li>
</ul>
</li>
</ol>
<p data-start="0" data-end="117">Assuming you've saved the script as, for example, <code data-start="50" data-end="66">json_to_csv.py</code>, you would run it from the command line like this:</p>
<p data-start="0" data-end="117"><code class="!whitespace-pre language-bash">python json_to_csv.py input.json output.csv</code></p>
<p data-start="176" data-end="394" data-is-last-node="" data-is-only-node="">Replace <code data-start="184" data-end="196">input.json</code> with the path to your JSON file and <code data-start="233" data-end="245">output.csv</code> with the desired path for the CSV output. If you're using Python 3 and your system requires it, you might need to use <code data-start="364" data-end="373">python3</code> instead of <code data-start="385" data-end="393">python</code>.</p>
