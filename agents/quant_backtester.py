import bt

def run_simple_backtest(
    strategy_name="SMA Cross", tickers=["AAPL"], sma_short=20, sma_long=50
):
    def strategy_logic():
        prices = bt.get(tickers, start="2020-01-01")
        sma_s = prices.rolling(sma_short).mean()
        sma_l = prices.rolling(sma_long).mean()
        return bt.Strategy(
            strategy_name,
            [
                bt.algos.SelectAll(),
                bt.algos.WeighEqually(),
                bt.algos.Rebalance(),
            ]
        )

    s = strategy_logic()
    data = bt.get(tickers)
    test = bt.Backtest(s, data)
    return bt.run(test)
