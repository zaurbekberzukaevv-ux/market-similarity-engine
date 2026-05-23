import pandas as pd

def build_windows(
    df:pd.DataFrame,
    window_size: int
):
    windows = []

    for start_idx in range(
        len(df) - window_size + 1 
    ):
        end_idx = start_idx + window_size
        window = df.iloc[
            start_idx:end_idx
        ]
        windows.append(window)
    return windows

