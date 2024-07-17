import gzip
from collections import Counter
from Bio import SeqIO

# Function to read the indexes from a FASTQ file
def read_indexes(file_path):
    indexes = []
    try:
        with gzip.open(file_path, "rt") if file_path.endswith(".gz") else open(file_path, "r") as handle:
            for record in SeqIO.parse(handle, "fastq"):
                # Extract the part after the space and split by '+'
                try:
                    # Split by space to get the identifier part with the indexes
                    index_part = record.description.split()[1]
                    # Split by '+' to separate the R1 and R2 indexes
                    index_r1, index_r2 = index_part.split('+')
                    indexes.append((index_r1, index_r2))
                except ValueError as e:
                    print(f"Skipping record {record.id} due to parsing error: {e}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return indexes

# Read indexes from both R1 and R2 files
r1_file_path = "Undetermined_S0_R1_001.fastq"
r2_file_path = "Undetermined_S0_R2_001.fastq"

print(f"Reading indexes from {r1_file_path}")
indexes_r1 = read_indexes(r1_file_path)
print(f"Found {len(indexes_r1)} indexes in {r1_file_path}")

print(f"Reading indexes from {r2_file_path}")
indexes_r2 = read_indexes(r2_file_path)
print(f"Found {len(indexes_r2)} indexes in {r2_file_path}")

# Combine paired indexes
paired_indexes = list(zip(indexes_r1, indexes_r2))
print(f"Total paired indexes: {len(paired_indexes)}")

# Count the frequency of each paired index
paired_index_counts = Counter(paired_indexes)
print(f"Unique paired indexes: {len(paired_index_counts)}")

# Get the top 1000 most common paired indexes
top_1000_paired_indexes = paired_index_counts.most_common(1000)
print(f"Top 1000 paired indexes: {len(top_1000_paired_indexes)}")

# Open output file for writing
output_file_path = "top_1000_paired_indexes.txt"
with open(output_file_path, "w") as output_file:
    # Print and write the results to the file
    for index_pair, count in top_1000_paired_indexes:
        result_line = f"{index_pair[0][0]} {index_pair[0][1]}: {count}\n"
        print(result_line, end="")
        output_file.write(result_line)

print(f"Results written to {output_file_path}")