import pandas as pd

class MarketWindow:
    
    def __repr__(self):

        return (
            f"MarketWindow("
            f"id={self.window_id}, "
            f"size={self.window_size})"
        )

    def __init__(
        self,
        window_id:int,
        data: pd.DataFrame
    ):
        """
        Конструктор объекта MarketWindow.

        Параметры:
        windod_id - уникальный номер окна
        data - DataFrame со свечами окна
        """

        self.window_id = window_id
        self.data = data

        self.start_time = self.data["date"].iloc[0]
        self.end_time = self.data["date"].iloc[-1]
        self.window_size = len(self.data)
        self.features = None
   
    