import pandas as pd

def load_market_data(path:str) -> pd.DataFrame :
    df = pd.read_csv(path)

    df["date"] = pd.to_datetime(
        df["date"],
        utc=True
    )
    return df