import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Select students_id = 101
    result = students[students['student_id'] == 101]
    # return corresponding columns of name and age only
    return result[['name', 'age']]