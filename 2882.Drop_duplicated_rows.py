import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicated email and keep the first id
    customers = customers.drop_duplicates(subset='email', keep='first')
    return customers