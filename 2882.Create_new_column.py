import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Add a column of bonus that contains the doubled values of salary
    employees['bonus']= employees['salary'] * 2
    # Return the data frame
    return employees