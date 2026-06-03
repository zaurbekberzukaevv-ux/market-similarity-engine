class SimilaritySearch:

    def __init__(
        self,
        historical_dataset,
        similarity_metric
    ):
        self.historical_dataset = historical_dataset
        self.similarity_metric = similarity_metric

    
    def _calculate_scores(
        self,
        target_vector
    ):
        results = []
        for _, row in self.historical_dataset.iterrows():
            window_id = row["window_id"]
            condidate_vector = row.drop(labels=["window_id"])
            
            similarity_score = self.similarity_metric.calculate(target_vector,condidate_vector)
            print(window_id)
            print(type(window_id))
            results.append(
                {
                    "window_id" : window_id,
                    "similarity_score" : similarity_score
                }
            )
        return results
        


    def _filter_neighbors(
        self,
        results,
        target_window_id,
        exclusion_radius
    ):
        filtered_results = []
        for result in results:
            window_id = result["window_id"]
            if abs(
                window_id - target_window_id 
            )<= exclusion_radius:
                continue
            filtered_results.append(result)

        return filtered_results

    def _sort_results(
        self,
        results
    ):
        pass

    def find_similar(
        self,
        target_vector,
        target_window_id,
        top_n,
        exclusion_radius
    ):
        pass