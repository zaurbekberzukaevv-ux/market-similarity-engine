from src.data.load_market_data import load_market_data
from src.data.validate_data import validate_dataset


print("Market Similarity Engine")

df = load_market_data(
    "data/raw/ETHUSDT_30m_fixed.csv"
)

validate_dataset(df)

