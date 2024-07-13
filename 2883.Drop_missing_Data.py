import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Use the dropna method to remove rows in name column
    students = students.dropna(subset=['name'])
    # Return the data frame after removing missing value
    return students
