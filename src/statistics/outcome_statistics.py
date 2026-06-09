class OutcomeStatistics:

    def __init__(
        self,
        outcomes_dataset
    ):
        self.outcomes_dataset = outcomes_dataset

    def _get_similar_outcomes(
        self,
        similar_windows
    ):
        window_ids = [window["window_id"] for window in similar_windows]
        similar_outcomes = self.outcomes_dataset[self.outcomes_dataset["window_id"].isin(window_ids)]
        return similar_outcomes

    def calculate_mean_return(
        self,
        similar_windows
    ):
        similar_outcomes = self._get_similar_outcomes(similar_windows)
        mean_return = similar_outcomes["final_return"].mean()
        return mean_return

    def calculate_median_return(
        self,
        similar_windows
    ):
        similar_outcomes = self._get_similar_outcomes(similar_windows)
        median_return = similar_outcomes["final_return"].median()
        return median_return

    def calculate_probability_above_threshold(
        self,
        similar_windows,
        threshold
    ):
        similar_outcomes = self._get_similar_outcomes(similar_windows)
        if similar_outcomes.shape[0] == 0:
            return 0.0
        probability = similar_outcomes[similar_outcomes["final_return"] > threshold].shape[0] / similar_outcomes.shape[0]
        return probability

    def calculate_mean_mfe(
        self,
        similar_windows
    ):
        similar_outcomes = self._get_similar_outcomes(similar_windows)
        mean_mfe = similar_outcomes["mfe"].mean()
        return mean_mfe

    def calculate_mean_mae(
        self,
        similar_windows
    ):
        similar_outcomes = self._get_similar_outcomes(similar_windows)
        mean_mae = similar_outcomes["mae"].mean()
        return mean_mae

    def calculate_quantiles(
        self,
        similar_windows,
        column_name,
        quantiles
    ):
        similar_outcomes = self._get_similar_outcomes(similar_windows)
        if len(similar_outcomes) == 0:
            return np.nan
        result = similar_outcomes[column_name].quantile(quantiles)
        return result