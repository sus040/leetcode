import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Replace missing data with 0 using fillna method
    products['quantity'] = products['quantity'].fillna(0)
    # Return updated data frame
    return products
