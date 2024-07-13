import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Update salary column by multiplying each salary by 2 
    employees['salary'] = employees['salary']*2
    # Return the updated data frame
    return employees