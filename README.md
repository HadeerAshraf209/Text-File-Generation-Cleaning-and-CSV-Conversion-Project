# Text File Generation, Cleaning, and CSV Conversion Project

## Overview
This project demonstrates a process for generating text files, modifying their content by inserting random symbols, cleaning the text by removing specific punctuation, converting the cleaned text files into CSV format, and merging these CSV files into a single file. 
The code is written in Python and utilizes various libraries such as os, re, random, csv, glob, and pandas.

## Features
* Text File Generation: Automatically creates 10 text files, each with a unique ID and space reserved for a name.
* Name Modification: Inserts randomly chosen symbols at random positions within a given name and writes the modified name into the text files.
* Text Cleaning: Removes specific punctuation marks from the content of the text files.
* Conversion to CSV: Converts the cleaned text files into CSV format.
* CSV Merging: Merges all individual CSV files into a single consolidated CSV file.

## Project Structure
10Files Folder: Contains the generated text files, cleaned text files, and the final CSV files.
Python Script: The script that performs all operations from file generation to CSV merging.

## Usage
### 1. Text File Generation
The script generates 10 text files in the 10Files directory. Each file is named file1.txt, file2.txt, ..., file10.txt.
```
generate_txt()
```
### 2. Name Modification
Randomly chosen symbols are inserted into the name "Hadeer Ashraf" at random positions and appended to each of the text files.
```
write_my_name()
```
### 3. Text Cleaning
The script removes specific punctuation marks (@, /, ., !, }, ;) from the text files.
````
cleaning_files(file_path)
````
### 4. Conversion to CSV
The cleaned text files are converted to CSV format, with each CSV file named cleaned_file1.csv, cleaned_file2.csv, etc.
````
convert_to_csv()
````
### 5. Merging CSV Files
All CSV files are merged into a single CSV file named combined.csv.
````
merge_csv_files()
````


## Installation
- Clone the repository to your local machine.
- Ensure you have the required Python libraries installed:
  * os
  * re
  * random
  * csv
  * pandas
  * glob
- Run the script to perform all operations.
