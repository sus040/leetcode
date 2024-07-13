import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Use the shape attribute 
    rows, columns = players.shape
    # Return rows and columns in list format
    return [rows, columns]