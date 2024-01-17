import pandas as pd
import sys

def concatenate_excel_files(file1, file2, output_file):
    # Read the data from the two Excel files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Concatenate the dataframes, ignoring the index
    result_df = pd.concat([df1, df2], ignore_index=True)

    # Write the concatenated dataframe to a new Excel file
    result_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python concatenate_excel.py <file1.xlsx> <file2.xlsx> <output_file.xlsx>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]

    concatenate_excel_files(file1, file2, output_file)
