class FeatureExtractor:

    def calculate_returns(
        self,
        close_prices
    ):
        #close_prices = window.data["close"]
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
        
        volatility = returns.std()

        return volatility

    def calculate_average_volume(
        self,
        volume
    ):

        return volume.mean()

    
    def calculate_trend_strength(
        self,
        window_return,
        volatility
    ):
        trend_strength = window_return/volatility
        return trend_strength


    def calculate_max_drawdown(
        self,
        close_prices
    ):
        running_max = close_prices.cummax()
        drawdowns = (close_prices/running_max)-1

        return drawdowns.min()


    def extract(
        self,
        window
    ):
        close_prices = window.data["close"]
        volume = window.data["volume"]
        returns = self.calculate_returns(close_prices)
        window_return = self.calculate_window_return(returns)
        volatility = self.calculate_volatility(returns)
        trend_strength = self.calculate_trend_strength(window_return,volatility)
        max_drawdown = self.calculate_max_drawdown(close_prices)
        return {
            "return" : window_return,
            "volatility" : volatility,
            "average_volume" : self.calculate_average_volume(volume),
            "trend_strength" : trend_strength,
            "max_drawdown" : max_drawdown
        }