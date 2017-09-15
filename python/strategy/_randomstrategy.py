from ._classes import Strategy, Order

class RandomStrategy(Strategy):

    def __init__(self, money, portfolio, from_date, to_date):
        super().__init__(money, portfolio, from_date, to_date)

    def execute(self, today):
        super().execute(today)

        ticker = self.get_instrument('OBX.OSE')

        order = Order(ticker, "buy", 100, 640)
        
        return [order]