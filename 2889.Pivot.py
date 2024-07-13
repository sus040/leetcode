import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Pivot the data to show temperature for each city in month order 
    result = weather.pivot(index='month', columns='city', values='temperature')
    # Return updated data frame
    return result
    
    