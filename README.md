# top_1000_indexes_from_fastq

This repository contains a Python script to extract the top 1000 paired indexes from paired-end FASTQ files of undetermined sequences (indexes not matching with any sample). The script reads the indexes from the provided FASTQ files, combines paired indexes, counts their frequencies, and outputs the top 1000 paired indexes along with their frequencies.

## Files in this Repository

- `extract_top_1000_indexes.py`: The Python script to extract the top 1000 paired indexes.

## Requirements

- Python 3.x
- Biopython

## Installation

To install the required Python library, run:

```bash
pip install biopython


## Usage
Prepare your FASTQ files: Ensure you have your paired-end FASTQ files named Undetermined_S0_R1_001.fastq and Undetermined_S0_R2_001.fastq.

Place the FASTQ files: Place the FASTQ files in the same directory as the script or provide the correct path to them.

Run the script: Execute the script using Python:

python extract_top_1000_indexes.py

## Output
The script will print the top 1000 paired indexes along with their frequencies on the screen and write them to an output file named top_1000_paired_indexes.txt.

Example Output
The output file top_1000_paired_indexes.txt will have the following format:

NAGTTCGGTA NCATGTGTAG: 150
NCTTAGTATA NCTTTCCCTA: 140
...

## Citation

If you use this script for your research, please consider citing it as follows:
Sharma, V. (2024). extract_top_1000_indexes.py [Python script]. Retrieved from https://github.com/vsmicrogenomics/top_1000_indexes_from_fastq

