
# Required libraries
import os, re, random, csv
from glob import iglob
import pandas as pd


# Creating a folder
try:
  path = os.mkdir(r"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2")
except FileExistsError:
  print('Directory already exists')


# Generate 10 txt files

def generate_txt():
    n = 1
    while n <= 10:
        print(f"Creating file{n}.txt")
        yield n
        with open(fr"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\file{n}.txt", 'w') as file:
            file.write(f"ID, {n}, Name, ")
        n += 1

generate_txt ()


list(generate_txt ())


# Generate name with symbols

def generate_name_with_symbols(name):
   # List of symbols
   symbols = ["@", "/", ".", "!", "}", ";"]

   while  True:
     # Choose 3 random symbols
      choosen_symbols = random.sample(symbols, 3)

      # Choose random positin inside the name
      positions = random.sample(range(len(name)), 3)
      positions.sort()

      # Insert symbols
      name_with_symbols =(
         name[:positions[0]] + choosen_symbols[0] +
         name[positions[0]: positions[1]] + choosen_symbols[1] +
         name[positions[1]: positions[2]] + choosen_symbols[2] +
         name[positions[2]:]
      )
    
      """
        position 1 = 4, name[:4] return Hade 
        then add the first symbol from the list 
        then add name[4:] which return eer 
      """

      yield name_with_symbols


# Write name with symbols in txt files
def write_my_name():
    name = "Hadeer Ashraf"
    name_generator = generate_name_with_symbols(name)

    for n in range(1,11):
        file_path = fr"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\file{n}.txt"

        with open(file_path, 'a') as txt_files:
            txt_files.write(f"{next(name_generator)}")


write_my_name()

# Reading txt files
read_txt_files = iglob(r"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\*.txt")


# Regex to match punctuation 
r = re.compile(r'[@/.!};]')



# Cleaning files content
def cleaning_files(file_path):
    with open(file_path) as clean_file:
        no_punc = r.sub("",clean_file.read())
        return no_punc.split()


# Reading and cleaning txt files
for file_path in iglob(r"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\*.txt"):
    
    with open(file_path) as original_ID:
        id_number = original_ID.readline().strip().split(",")[1].strip()

    cleaned_content = cleaning_files(file_path)
    str_cleaned_content = " ".join(cleaned_content)
    
    # New file path to write the clean content
    new_file_path = fr"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\cleaned_file{id_number}.txt"
    with open(new_file_path, 'w') as clean_file:
        clean_file.write(str_cleaned_content)

print("Cleaning and writing to new files completed")


# Convert cleaned txt files to csv

def convert_to_csv():
    for file_path in iglob(r"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\cleaned_file*.txt"):

        with open(file_path, "r") as input_txt:
            read_content = input_txt.read()
            data = read_content.split(",")

            id_number = data[1]. strip()

            csv_file_path = fr"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\cleaned_file{id_number}.csv"

            with open(csv_file_path, "w") as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(data)

    print("Conversion completed")

convert_to_csv()    


# Create function to merge CSV file into one 

def merge_csv_files():
    # Empty list of DataFrames for csv files
    csv_dataframes = []

    for file_path in iglob(r"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\cleaned_file*.csv"):
        df = pd.read_csv(file_path, names = ["A", "ID", "C", "Name"])
        df = df [["ID", "Name"]]

        csv_dataframes.append(df)

    # Combine all list elemens into one dataframe
    combined_df = pd.concat(csv_dataframes)
    combined_df.to_csv(r"C:\Users\Hadeer Ashraf\OneDrive\Desktop\DEPI - MS Data Engineer\PYTHON\10_Files_V2\combined.csv", index=False)

    print("Merging completed")

    
merge_csv_files()



