# Exercise 8.1

import csv

# Used to open and read the csv file
with open('sample_data.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    
    # Goes through the csv file and outputs the data in rows
    for row in csv_reader:
        print(row)
        
# Exercise 8.2

import csv

with open('sample_data.csv', mode='r', newline='', encoding='utf-8') as file:
    # Used to read the CSV file as a dictionary
    csv_dict_reader = csv.DictReader(file)
    
    #Output the data and filling the data in the print statement line-by-line
    for row in csv_dict_reader:
        print(f"{row['name']} is a {row['age']}-year-old {row['role']} from {row['city']}.")
        
        
# Exercise 8.3

# a) 3 people (Ada, Alan, Linus) are engineers.

# b) The average age of everyone in the file is 36.83.

# Exercise 8.4

import pandas as pd

df = pd.read_csv("sample_data.csv") #Used to read the csv file in tabular form
print(df.head()) #Prints the layout of the csv file
print(df["age"].mean()) #Calculates the mean age of everyone mentioned in the CSV file
