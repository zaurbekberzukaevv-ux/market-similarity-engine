import numpy as np

class SimilarityMetric:

    def calculate(
        self,
        vector_a,
        vector_b
    ):
        array_a = vector_a.to_numpy()
        array_b = vector_b.to_numpy()
 
        norm_a = np.linalg.norm(array_a)
        norm_b = np.linalg.norm(array_b)

        if norm_a==0 or norm_b == 0:
            raise ValueError("Cannot calculate cosine similarity for zero-length vector")
        dot_product = np.dot(array_a, array_b)

        similarity_score = dot_product/(norm_a*norm_b)

        return similarity_score
