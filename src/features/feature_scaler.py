class FeatureScaler:
    def __init__(
        self
    ):
        self.means = None
        self.stds = None

    def fit(
        self,
        feature_dataset
    ):
        features_only = feature_dataset.drop(
        columns=["window_id"]
    )
        self.means = features_only.mean()
        self.stds = features_only.std()

    def transform(
        self,
        feature_dataset
    ):
        features_only = feature_dataset.drop(
        columns=["window_id"]
    )
        scaled_dataset =  (features_only-self.means)/self.stds
        scaled_dataset["window_id"] = feature_dataset["window_id"]
        return scaled_dataset