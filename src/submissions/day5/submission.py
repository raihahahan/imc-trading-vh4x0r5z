from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order
import pandas as pd
import numpy as np


class Trader:
    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        # Initialize the method output dict as an empty dict
        result = {}
        
        # Get order depths for all symbols in the current state
        order_depths = state.order_depths
        
        for symbol, depth in order_depths.items():
            # Get buy and sell orders for the current symbol
            buy_orders = depth.buy_orders
            sell_orders = depth.sell_orders
            
            # Convert the buy and sell order dictionaries to dataframes
            buy_df = pd.DataFrame(list(buy_orders.items()), columns=['Price', 'Quantity'])
            sell_df = pd.DataFrame(list(sell_orders.items()), columns=['Price', 'Quantity'])
            
            # Sort the buy and sell dataframes by price
            buy_df.sort_values(by=['Price'], ascending=False, inplace=True)
            sell_df.sort_values(by=['Price'], ascending=True, inplace=True)
            
            # Compute the mid price as the average of the best bid and best ask prices
            best_bid_price = buy_df['Price'].iloc[0] if not buy_df.empty else 0
            best_ask_price = sell_df['Price'].iloc[0] if not sell_df.empty else float('inf')
            mid_price = (best_bid_price + best_ask_price) / 2
            
            # Compute the buy and sell order quantities to reach the desired position
            desired_position = state.position[symbol]
            current_position = state.observations[state.listings[symbol].product]
            net_position = desired_position - current_position
            
            if net_position > 0:
                # We need to buy more of the symbol to reach the desired position
                
                # Set the buy price as the mid price minus a small margin
                buy_price = mid_price - 1
                
                # Calculate the buy order quantity as a function of the net position and the buy price
                buy_order_quantity = min(net_position, int(state.observations[state.listings[symbol].denomination] / buy_price))
                
                # Create a buy order for the current symbol with the calculated price and quantity
                buy_order = Order(symbol, buy_price, buy_order_quantity)
                
                # Add the buy order to the method output dict for the current symbol
                result[symbol] = [buy_order]
                
            elif net_position < 0:
                # We need to sell some of the symbol to reach the desired position
                
                # Set the sell price as the mid price plus a small margin
                sell_price = mid_price + 1
                
                # Calculate the sell order quantity as a function of the net position and the sell price
                sell_order_quantity = min(abs(net_position), state.observations[state.listings[symbol].product])
                
                # Create a sell order for the current symbol with the calculated price and quantity
                sell_order = Order(symbol, sell_price, sell_order_quantity)
                
                # Add the sell order to the method output dict for the current symbol
                result[symbol] = [sell_order]
                
        return result