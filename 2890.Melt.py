import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # Use melt method to reshape the data
    melted_df = report.melt(
    id_vars = ['product'], # Define identifier
    var_name = 'quarter', # Define variable names 
    value_name = 'sales') # Set a column with sales variables
    # Return melted data frame 
    return melted_df