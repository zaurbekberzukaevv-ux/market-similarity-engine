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
        self.means = feature_dataset.mean()
        self.stds = feature_dataset.std()

    def transform(
        self,
        feature_dataset
    ):
        scaled_dataset =  (feature_dataset-self.means)/self.stds

        return scaled_dataset