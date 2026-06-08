from src.data.load_market_data import load_market_data
from src.data.validate_data import validate_dataset
from src.windows.window_builder import build_windows
from src.windows.market_window import MarketWindow
from src.features.feature_extractor import FeatureExtractor
import pandas as pd
from src.features.feature_pipeline import FeaturePipeline
from src.features.feature_scaler import FeatureScaler
from src.similarity.similarity_metric import SimilarityMetric
from src.outcomes.outcome_engine import OutcomeEngine

print("Market Similarity Engine")

df = load_market_data(
    "data/raw/ETHUSDT_30m_fixed.csv"
)

#validate_dataset(df)

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
    windows[0].data["close"]
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

pipeline = FeaturePipeline(
    extractor
)
feature_dataset = pipeline.build_feature_dataset(
    windows[:5]
)
print(type(feature_dataset))
print(feature_dataset.head())

scaler = FeatureScaler()

scaler.fit(
    feature_dataset
)

scaled_dataset = scaler.transform(
    feature_dataset
)

print(
    scaled_dataset.head()
)

print(type(scaled_dataset.iloc[0]))

similarity = SimilarityMetric()
print(similarity.calculate(
    scaled_dataset.iloc[0],
    scaled_dataset.iloc[1]
))

print(feature_dataset.head())

from src.similarity.similarity_search import SimilaritySearch

search = SimilaritySearch(
    historical_dataset=scaled_dataset,
    similarity_metric=similarity
)

target_vector = scaled_dataset.iloc[0].drop(
    labels=["window_id"]
)

results = search._calculate_scores(
    target_vector
)

print(type(results))
print(len(results))
print(results[0])
print(type(results[0]))

print(scaled_dataset.dtypes)

from src.similarity.similarity_search import SimilaritySearch

search = SimilaritySearch(
    historical_dataset=scaled_dataset,
    similarity_metric=similarity
)

results = search.find_similar(
    target_vector=scaled_dataset.iloc[0].drop(labels=["window_id"]),
    target_window_id=0,
    top_n=3,
    exclusion_radius=1
)

print(results)
print(type(results))
print(len(results))

outcome_engine = OutcomeEngine(
    historical_dataset=df,
    horizon=10,
    window_size=20
)

outcomes_dataset = outcome_engine.create_outcomes_dataset()

print(type(outcomes_dataset))

print(outcomes_dataset.head())

print(outcomes_dataset.tail())

print(outcomes_dataset.shape)

print(outcomes_dataset.dtypes)
# test = pd.Series([
#     None,
#     0.1,
#     0.1,
#     -0.099
# ])
# print(test)
# print(test+1)
# print((test+1).prod())