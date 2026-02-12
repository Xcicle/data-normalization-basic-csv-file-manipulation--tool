import pandas as pd

class Normalizer:
    # Initialize with the original CSV file and an empty dictionary for tables
    def __init__(self):
        self.df = pd.read_csv("school_records.csv")
        self.tables = {}  # Stores created tables as DataFrames

    # Display number of records and check for duplicates in a column
    def display_column_info(self, index):
        print(
            f"\nThe number of records in column '{self.df.columns[index - 1]}' is {self.df[self.df.columns[index - 1]].count()}")
        if self.df[self.df.columns[index - 1]].duplicated().any():
            print(f"There are duplicate records in column '{self.df.columns[index - 1]}'")
        else:
            print(f"There are no duplicate records in column '{self.df.columns[index - 1]}'")

    # Allow user to find column by name or index and display info
    def find_column(self):
        column = input("\nEnter the column's name or the column's index: ")
        if column.isdigit() and int(column) <= len(self.df.columns):
            self.display_column_info(int(column))
        elif column.isdigit() and int(column) not in range(1, len(self.df.columns)+1):
            print(f"Column not found: Index - {column}")
        elif column.isalpha():
            found = False
            for i in range(0, len(self.df.columns)):
                if self.df.columns[i] == column:
                    found = True
                    self.display_column_info(i+1)
            if not found:
                print(f"Column not found: Name - {column}")

    # Create a new table from selected columns of the original CSV
    def create_table(self):
        num = int(input("\nEnter the number of columns for this table: "))
        columns = []

        # Ask user for column names and validate
        for i in range(1, num + 1):
            while True:
                name = input(f"Enter the name of column No.{i} from the original table:")
                if name in self.df.columns and name not in columns:
                    columns.append(name)
                    break
                else:
                    print(f"\nColumn not found: '{name}'. Please try again.\n")

        table_name = input("Enter the name of the table: ").strip()

        # Copy selected columns and remove duplicates
        self.tables[table_name] = self.df[columns].drop_duplicates()

        print(f"\nTable '{table_name}' created.")
        print("Columns:", columns)

        # Save the table as a new CSV
        self.tables[table_name].to_csv(f"{table_name}.csv", index=False)
        print(f"\n{table_name}.csv has been saved.\n")

    # Modify an existing table CSV (add/remove columns, edit records, reorder)
    def modify_table(self):
        table_name = input("\nEnter the name of the table to modify: ")
        while True:
            try:
                df_temp = pd.read_csv(f"{table_name}.csv")  # Load table
            except FileNotFoundError:
                print(f"\n{table_name}.csv file not found. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Try again")
            else:
                break

        while True:
            # Display modification menu
            print('=======================================')
            print("| Modification Name       |  Func No. |")
            print("---------------------------------------")
            print("| Add Column              |     1     |")
            print("| Remove Column           |     2     |")
            print("| Modify specific record  |     3     |")
            print("| Re-order Columns        |     4     |")
            print("| Exit modification       |     5     |")
            print('=======================================')
            func_num = input("\nEnter function number: ")

            if func_num == "1":
                # Add a new column (copy from original if exists, else use default)
                col_name = input("Enter new column name: ")
                default = input("Enter default value: ")
                if col_name in self.df.columns:
                    df_temp[col_name] = self.df[col_name].fillna(default)
                else:
                    df_temp[col_name] = default

            elif func_num == "2":
                # Remove a column (cannot remove last column)
                col_name = input("Enter name of the column to remove: ")
                if len(df_temp.columns) == 1:
                    print("Cannot remove the last column")
                elif col_name in df_temp.columns:
                    df_temp.drop(col_name, axis=1, inplace=True)
                else:
                    print(f"\nColumn not found: '{col_name}'. Please try again.\n")

            elif func_num == "3":
                # Modify a specific record
                row = int(input("Enter row index: "))
                col = input("Enter column name: ")
                value = input("Enter new value: ")
                if row in df_temp.index and col in df_temp.columns:
                    df_temp.at[row, col] = value
                else:
                    print("Invalid row or column.")

            elif func_num == "4":
                # Reorder columns
                print(f'Current column positions: {df_temp.columns}')
                new_positions = []
                for i in range(0, len(df_temp.columns)):
                    while True:
                        position = input(f"Enter the name of the column for position No.{i+1}: ")
                        if position not in df_temp.columns:
                            print(f"Column not found: '{position}'. Please try again.\n")
                        elif position in new_positions:
                            print(f"Column '{position}' already entered. Choose another.\n")
                        else:
                            new_positions.append(position)
                            break
                df_temp = df_temp[new_positions]
                df_temp.to_csv(f"{table_name}.csv", index=False)

            elif func_num == "5":
                # Save changes and exit modification menu
                df_temp.to_csv(f"{table_name}.csv", index=False)
                print("Changes saved. Exiting modification program.\n")
                break
