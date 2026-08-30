import pandas as pd
from pathlib import Path
from student import *

def main():
    input_string = input('Question Input (ex."Q1") : ').strip() 
    csv_path = Path(__file__).with_name('titanic_to_student.csv')
    df = pd.read_csv(csv_path, index_col=0)
    if input_string == "Q7":
        df.fillna(df.select_dtypes(
            include='number').mean(), inplace=True)
    input_command = f"{input_string}(df)"
    print(f"Your Answer: {eval(input_command)}")


if __name__ == "__main__":
    main()
