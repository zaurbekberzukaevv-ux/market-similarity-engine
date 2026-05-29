class FeatureExtractor:

    def calculate_returns(
        self,
        window
    ):
        close_prices = window.data["close"]
        returns = close_prices.pct_change()
        return returns

    def calculate_window_return(
        self,
        returns
    ):
        """
        Извлекает признаки из MarketWindow.
        Пока считаем только доходность окна.
        """
        #returns = self.calculate_returns(window)
        growth_factors = returns+1
        total_growth = growth_factors.prod()
        window_return = total_growth - 1

        return window_return


    def calculate_volatility(
        self,
        returns
    ):
        #returns = self.calculate_returns(window)
        volatility = returns.std()

        return volatility
    
    def extract(
        self,
        window
    ):
        returns = self.calculate_returns(window)
        return {
            "return" : self.calculate_window_return(returns),
            "volatility" : self.calculate_volatility(returns)
        }