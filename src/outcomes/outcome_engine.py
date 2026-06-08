import pandas as pd
import numpy as np

class OutcomeEngine:
    def __init__(
        self,
        historical_dataset,
        horizon,
        window_size,
    ):
        self.historical_dataset = historical_dataset
        self.horizon = horizon
        self.window_size = window_size

    def create_outcomes_dataset(
        self,
    ):
        outcomes = []
        for window_id in range(len(self.historical_dataset)-self.window_size-self.horizon+1):
            outcome = self._calculate_outcome(window_id)
            outcomes.append(outcome)
        return pd.DataFrame(outcomes)

    def _calculate_outcome(
        self,
        window_id
    ):
        end_index = window_id + self.window_size - 1
        future_start = end_index + 1
        future_end = future_start + self.horizon - 1
        if future_end >= len(self.historical_dataset):

            return {

                "window_id": window_id,
                "final_return": np.nan,
                "mfe": np.nan,
                "mae": np.nan
            }
        entry_price = self.historical_dataset.iloc[end_index]["close"]
        future_prices = self.historical_dataset.iloc[future_start:future_end+1]["close"]

        final_return = self._calculate_final_return(entry_price, future_prices)
        mfe = self._calculate_mfe(entry_price, future_prices)
        mae = self._calculate_mae(entry_price, future_prices)
        return {
            "window_id": window_id,
            "final_return": final_return,
            "mfe": mfe,
            "mae": mae
        }

    def _calculate_final_return(
        self,
        entry_price,
        future_prices
    ):
        last_price = future_prices.iloc[-1]
        final_return = (last_price/entry_price)-1
        return final_return

    def _calculate_mfe(
        self,
        entry_price,
        future_prices
    ):
        max_price = future_prices.max()
        mfe = (max_price/entry_price)-1
        return mfe

    def _calculate_mae(
        self,
        entry_price,
        future_prices
    ):
        min_price = future_prices.min()
        mae = (min_price/entry_price)-1
        return mae
