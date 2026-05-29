import pandas as pd
class FeaturePipeline:
    def __init__(
        self,
        extractor
    ):
        self.extractor = extractor

    def build_feature_dataset(
        self,
        windows
    ):
        features = []
        for window in windows:
            features.append(self.extractor.extract(window))
        all_features = pd.DataFrame(features)
        return all_features
