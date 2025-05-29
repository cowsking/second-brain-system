import os
import glob

# Define the folder containing the CSV files
folder_path = 'lifelogs'
output_file = 'all_csv.csv'

# Get all .csv files in the specified folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate through each CSV file
    for csv_file in csv_files:
        # Open each file in read mode
        with open(csv_file, 'r') as infile:
            # Read the content and write it to the output file
            outfile.write(infile.read())
            outfile.write('\n')  # Optional: add a newline between files

print(f'All CSV files have been combined into {output_file}.')
