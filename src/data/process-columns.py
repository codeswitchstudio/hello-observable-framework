import csv

# Input data (replace with the actual file path)
input_file = "/Users/lseideas/Documents/Indira-MBAir/Dev/hello-observable-framework/src/data/rplife.csv"
output_file = "/Users/lseideas/Documents/Indira-MBAir/Dev/hello-observable-framework/src/data/rplife02.csv"

# Read and transform the data
with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Read the header rows
    header1 = next(reader)  # First row: year,1800,1801,...
    header2 = next(reader)  # Second row: age,30.9,30.9,...
    
    # Write the new header
    writer.writerow(["year", "age"])
    
    # Combine years and ages into rows
    for year, age in zip(header1[1:], header2[1:]):  # Skip the first element ("year"/"age")
        writer.writerow([year, age])
