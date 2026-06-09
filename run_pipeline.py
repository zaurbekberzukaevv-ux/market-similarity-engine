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
from src.statistics.outcome_statistics import OutcomeStatistics
from src.similarity.similarity_search import SimilaritySearch
from src.similarity.similarity_search import SimilaritySearch
from src.analysis.market_analyzer import MarketAnalyzer

print("Market Similarity Engine")

df = load_market_data(
    "data/raw/ETHUSDT_30m_fixed.csv"
)

#validate_dataset(df)

windows = build_windows(
    df,
    window_size=20
)

print(type(windows))


extractor = FeatureExtractor()
print(type(extractor))

pipeline = FeaturePipeline(extractor)
feature_dataset = pipeline.build_feature_dataset(windows)
print(type(feature_dataset))

scaler = FeatureScaler()

scaler.fit(feature_dataset)

scaled_dataset = scaler.transform(feature_dataset)



print(type(scaled_dataset))

similarity = SimilarityMetric()

search = SimilaritySearch(historical_dataset=scaled_dataset,similarity_metric=similarity)

target_vector = scaled_dataset.iloc[0].drop(labels=["window_id"])

results = search._calculate_scores(target_vector)

print(type(results))

search = SimilaritySearch(historical_dataset=scaled_dataset,similarity_metric=similarity)

results = search.find_similar(
    target_vector=scaled_dataset.iloc[0].drop(labels=["window_id"]),
    target_window_id=0,
    top_n=20,
    exclusion_radius=20
)
print(type(results))

outcome_engine = OutcomeEngine(
    historical_dataset=df,
    horizon=10,
    window_size=20
)

outcomes_dataset = outcome_engine.create_outcomes_dataset()

statistics = OutcomeStatistics(
    outcomes_dataset
)
quantiles = statistics.calculate_quantiles(
    similar_windows=results,
    column_name="final_return",
    quantiles=[0.1, 0.25, 0.5, 0.75, 0.9]
)

print(quantiles)



statistics = OutcomeStatistics(
    outcomes_dataset
)

analyzer = MarketAnalyzer(
    similarity_search=search,
    outcome_statistics=statistics
)

report = analyzer.analyze(
    target_vector=scaled_dataset.iloc[0].drop(
        labels=["window_id"]
    ),
    target_window_id=0,
    top_n=20,
    exclusion_radius=20,
    threshold=0.01
)

print(report)
# test = pd.Series([
#     None,
#     0.1,
#     0.1,
#     -0.099
# ])
# print(test)
# print(test+1)
# print((test+1).prod())