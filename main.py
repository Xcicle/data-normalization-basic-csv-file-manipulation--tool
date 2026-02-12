import pandas as pd
from normalizer import Normalizer

norm = Normalizer()

df = pd.read_csv("school_records.csv")

print('============================================================================')

for i in range(0,len(df.columns)):
    print(f"| Column No.{i+1:<7}| {df.columns[i]:<16}|")
print('======================================\n')

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
        norm.create_table()
    elif func_num == "2":
        norm.find_column()
    elif func_num == "3":
        norm.modify_table()
    elif func_num == "4":
        print("\nExiting the program..")
        print('\n============================================================================')
        break


