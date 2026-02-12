import pandas as pd
from normalizer import Normalizer

"""
Data Normalisation Project
Author: Nathan
Description:
This program demonstrates data normalisation principles using Python and pandas.
It processes a dataset and separates structured data into organised tables.
"""



# Initialize the Normalizer class
norm = Normalizer()

# Load the original CSV to display columns
df = pd.read_csv("school_records.csv")

# Show all columns in the original table
print('============================================================================')
for i in range(0, len(df.columns)):
    print(f"| Column No.{i + 1:<7}| {df.columns[i]:<16}|")
print('======================================\n')

# Main interactive menu
while True:
    print('=======================================')
    print("| Function Name           |  Func No. |")
    print("---------------------------------------")
    print("| Create Table(csv)       |     1     |")
    print("| View a Column's Data    |     2     |")
    print("| Modify Table            |     3     |")
    print("| Exit program            |     4     |")
    print('=======================================')
    func_num = input("\nEnter function number: ")
    print("\n----------------------------------------------------------------------------")

    if func_num == "1":
        # Create a new table from selected columns
        norm.create_table()
    elif func_num == "2":
        # View information about a specific column
        norm.find_column()
    elif func_num == "3":
        # Modify an existing table
        norm.modify_table()
    elif func_num == "4":
        # Exit the program
        print("\nExiting the program..")
        print('\n============================================================================')
        break
