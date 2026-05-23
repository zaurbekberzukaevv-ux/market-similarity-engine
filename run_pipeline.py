from src.data.load_market_data import load_market_data
from src.data.validate_data import validate_dataset
from src.windows.window_builder import build_windows

print("Market Similarity Engine")

df = load_market_data(
    "data/raw/ETHUSDT_30m_fixed.csv"
)

validate_dataset(df)

windows = build_windows(
    df,
    window_size=20
)

print(
    f"Total windows: {len(windows)}"
)
print(windows[0])

