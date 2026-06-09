class MarketAnalyzer:

    def __init__(
        self,
        similarity_search,
        outcome_statistics
    ):
        # объект SimilaritySearch
        self.similarity_search = similarity_search

        # объект OutcomeStatistics
        self.outcome_statistics = outcome_statistics

    def analyze(
        self,
        target_vector,
        target_window_id,
        top_n,
        exclusion_radius,
        threshold
    ):
        # найти похожие окна
        
        similar_windows = self.similarity_search.find_similar(
            target_vector=target_vector,
            target_window_id=target_window_id,
            top_n=top_n,
            exclusion_radius=exclusion_radius
        )
        print(similar_windows)

        # посчитать среднюю доходность
        mean_return = self.outcome_statistics.calculate_mean_return(
            similar_windows
        )
        print(mean_return)
        # посчитать медианную доходность
        median_return = self.outcome_statistics.calculate_median_return(
            similar_windows
        )
        print(median_return)

        # посчитать средний MFE
        mean_mfe = self.outcome_statistics.calculate_mean_mfe(
            similar_windows
        )
        print(mean_mfe)
        # посчитать средний MAE
        mean_mae = self.outcome_statistics.calculate_mean_mae(
            similar_windows
        )
        print(mean_mae)
        # вероятность заработать больше заданного порога
        probability_above_threshold = self.outcome_statistics.calculate_probability_above_threshold(
            similar_windows,
            threshold
        )
        print(probability_above_threshold)
        # квантили доходности
        return_quantiles = self.outcome_statistics.calculate_quantiles(
            similar_windows,
            "final_return",
            [0.1, 0.25, 0.5, 0.75, 0.9]
        )
        print(return_quantiles)
        # собрать отчет
        report = {
            "similar_windows": similar_windows,
            "mean_return": mean_return,
            "median_return": median_return,
            "mean_mfe": mean_mfe,
            "mean_mae": mean_mae,
            "probability_above_threshold": probability_above_threshold,
            "return_quantiles": return_quantiles
        }

        return report
        print(similar_windows)

