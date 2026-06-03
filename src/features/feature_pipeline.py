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
            # Получаем словарь признаков для одного окна
            features_row = self.extractor.extract(window)

            #Добавляем служебный идентификатор окна
            features_row["window_id"] = window.window_id

            #добавляем уже дополненный словарь
            features.append(features_row)

            #features.append(self.extractor.extract(window))
            
        all_features = pd.DataFrame(features)
        return all_features
