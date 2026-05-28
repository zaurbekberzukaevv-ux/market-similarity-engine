from src.data.load_market_data import load_market_data
from src.data.validate_data import validate_dataset
from src.windows.window_builder import build_windows
from src.windows.market_window import MarketWindow
from src.features.feature_extractor import FeatureExtractor
import pandas as pd

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

market_window = windows[0]

print(type(market_window))
print(market_window.window_id)
print(type(market_window.data))

print(market_window.data.head(3))
print(len(market_window.data))

print(market_window.start_time)
print(market_window.end_time)
print(market_window.window_size)

extractor = FeatureExtractor()
print(type(extractor))

extractor = FeatureExtractor()

returns = extractor.calculate_returns(
    windows[0]
)

print(returns)
print(type(returns))
print(len(returns))

features = extractor.extract(
    windows[0]
)

windows[0].features = features
print(windows[0].features)

print(features)
print(type(features))
print(type(features["return"]))

# test = pd.Series([
#     None,
#     0.1,
#     0.1,
#     -0.099
# ])
# print(test)
# print(test+1)
# print((test+1).prod())