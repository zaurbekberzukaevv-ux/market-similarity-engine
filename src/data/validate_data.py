import pandas as pd

def find_time_gaps(df:pd.DataFrame):

    gaps = df[df["date"].diff() > pd.Timedelta(minutes=30)]

    return gaps

def analyze_time_gaps(df:pd.DataFrame):
     # Считаем разницу между соседними свечами
    diff = df["date"].diff()
    # Берём только проблемные места
    gaps = df[diff > pd.Timedelta(minutes=30)].copy()
    # Берём только проблемные места
    gaps["gap_size"] = diff[diff > pd.Timedelta(minutes=30)]

    gaps["missing_candles"] = (
        gaps["gap_size"] /
        pd.Timedelta(minutes=30)
    ) - 1
    return gaps

def validate_dataset(df):

    duplicates = df.duplicated().sum()

    print("\nDUPLICATES")
    print(duplicates)

    duplicate_dates = df["date"].duplicated().sum()

    print("\nDUPLICATE DATES")
    print(duplicate_dates)

    is_sorted = df["date"].is_monotonic_increasing

    print("\nSORTED")
    print(is_sorted)

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    print("\nNEGATIVE VALUES")

    print("open :", (df["open"] < 0).sum())
    print("high :", (df["high"] < 0).sum())
    print("low :", (df["low"] < 0).sum())
    print("close :", (df["close"] < 0).sum())
    print("volume :", (df["volume"] < 0).sum())

    invalid_high = (
        (df["high"] < df["open"]) |
        (df["high"] < df["close"])
    ).sum()

    invalid_low = (
        (df["low"] > df["open"]) |
        (df["low"] > df["close"])
    ).sum()

    print("\nINVALID OHLC")
    print("invalid high:", invalid_high)
    print("invalid low:", invalid_low)

    gaps = find_time_gaps(df)

    print("\nTIME GAPS")
    print(gaps[["date"]].head(20))

    gap_report = analyze_time_gaps(df)

    print("\nGAP REPORT")
    print(
        gap_report[
            ["date", "gap_size", "missing_candles"]
        ]
    )