# Concatenate Excel Files

This Python script is designed to concatenate two Excel files (in xlsx format) while ensuring that the header appears only once in the resulting file.

## Requirements

- python 3
- pandas
- openpyxl

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/maurodruwel/concatenate-excel-files.git
   ```

2. Navigate to the project directory:

    ```bash
    cd concatenate-excel-files
    ```

3. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the script from the command line by providing the paths of the two Excel files to be concatenated and the output file:

```bash
python concatenate_excel.py file1.xlsx file2.xlsx combined.xlsx
```

Make sure to replace **file1.xlsx**, **file2.xlsx**, and **combined.xlsx** with the actual file names.

The script will concatenate the files, keeping the header from the first file and excluding the header from the second file.

Have fun!😊