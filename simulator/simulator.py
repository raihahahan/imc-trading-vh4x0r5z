import pandas as pd

from typing import Dict, List
from datamodel import TradingState, Order
from .tradingStateGenerator import *
from .testAlgo import *

class Trader:

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        return run(state)
 

prices_file_path = "src\\day4\\data\\prices_round_4_day_1.csv"
trades_file_path = "src\\day4\\data\\trades_round_4_day_1_nn.csv"
tradingState = tradingStateGenerator(prices_file_path, trades_file_path)

trader = Trader()
result = trader.run(tradingState)

print(result)