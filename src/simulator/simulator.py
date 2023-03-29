import pandas as pd

from typing import Dict, List
from datamodel import TradingState, Order
from .tradingStateGenerator import *
from .testAlgo import *
from datetime import datetime
from .csv_utils import *

class Trader:
    # DO NOT CHANGE THE CODE INSIDE THIS TRADER CLASS
    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        return run(state)
    
def run_simulation(num_test: int, prices_file_path: str, trades_file_path: str):
    tradingState = tradingStateGenerator(prices_file_path, trades_file_path)
    trader = Trader()
    result = {}
    for i in range(num_test):
        res: Dict[str, List[Order]] = trader.run(tradingState)
        for k, v in res.items():
            if k in result:
                curr_trades: List[Order] = result[k]
                curr_trades.append(v)
            else:
                result[k] = v

    save_results_to_file(result)
    return result
        

 
## Modify the file paths
prices_files = ["src\submissions\day4\data\prices_round_4_day_1.csv", "src\submissions\day4\data\prices_round_4_day_2.csv", "src\submissions\day4\data\prices_round_4_day_3.csv" ]

trades_files = ["src\submissions\day4\data\\trades_round_4_day_1_nn.csv", "src\submissions\day4\data\\trades_round_4_day_2_nn.csv", "src\submissions\day4\data\\trades_round_4_day_3_nn.csv"]

combined_prices_csv_path = combine_csv_files(prices_files, "prices")
combined_trades_csv_path = combine_csv_files(trades_files, "trades")  

result = run_simulation(1000, prices_file_path=combined_prices_csv_path, trades_file_path=combined_trades_csv_path)
