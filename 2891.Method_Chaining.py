import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame for animals with weight greater than 100
    filtered_df = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)
    # Select the 'name' column
    result = filtered_df[['name']]
    # Return results table with name in descending order of weight
    return result
