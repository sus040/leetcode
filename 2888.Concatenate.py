import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate two dataframe vertically into one data frame
    final = pd.concat([df1, df2])
    # Return final column
    return final