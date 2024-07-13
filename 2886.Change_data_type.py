import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Convert data type to integer by using astype method
    students['grade'] = students['grade'].astype(int)
    # Return updated column
    return students