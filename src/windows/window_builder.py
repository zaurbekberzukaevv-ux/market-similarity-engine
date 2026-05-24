import pandas as pd
from src.windows.market_window import MarketWindow


def build_windows(
    df:pd.DataFrame,
    window_size: int
):
    windows = []

    for start_idx in range(
        len(df) - window_size + 1 
    ):
        end_idx = start_idx + window_size
        window_df = df.iloc[start_idx:end_idx]
        window = MarketWindow(
            start_idx,
            window_df
        )
        windows.append(window)
    return windows

