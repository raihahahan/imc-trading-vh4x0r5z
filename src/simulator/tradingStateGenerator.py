import csv
from collections import defaultdict
from typing import Dict
from datamodel import *

def tradingStateGenerator(prices_file_path: str, trades_file_path: str) -> TradingState:
    def get_listings(file_path: str) -> Dict[str, Listing]:
        result = {}
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            for row in csv_reader:
                symbol = row["product"]
                if symbol not in result:
                    result[symbol] = Listing(symbol=symbol, product=symbol, denomination="SEASHELLS")
        return result
    
    def get_order_depths(file_path: str) -> Dict[str, OrderDepth]:
        result = defaultdict(list)
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")

            for row in csv_reader:
                symbol = row["product"]
                if symbol not in result:
                    result[symbol] = OrderDepth()
                bid_prices = [float(row["bid_price_1"] or 0), float(row["bid_price_2"] or 0), float(row["bid_price_3"] or 0)]
                bid_volumes = [float(row["bid_volume_1"] or 0), float(row["bid_volume_2"] or 0), float(row["bid_volume_3"] or 0)]
                ask_prices = [float(row["ask_price_1"] or 0), float(row["ask_price_2"] or 0), float(row["ask_price_3"] or 0)]
                ask_volumes = [-float(row["ask_volume_1"] or 0), -float(row["ask_volume_2"] or 0), -float(row["ask_volume_3"] or 0)]
                for i in range(3):
                    if bid_volumes[i] > 0:
                        result[symbol].buy_orders[bid_prices[i]] = bid_volumes[i]
                    if ask_volumes[i] < 0:
                        result[symbol].sell_orders[ask_prices[i]] = ask_volumes[i]
        return result
    
    def get_trades(file_path: str) -> Dict[str, list]:
        result = defaultdict(list)
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            for row in csv_reader:
                symbol = row["symbol"]
                price = float(row["price"])
                quantity = float(row["quantity"])
                timestamp = row["timestamp"]
                trade = Trade(symbol=symbol, price=price, quantity=quantity, buyer="", seller="", timestamp=timestamp)
                result[symbol].append(trade)
        return result
    
    timestamp = 10000
    listings = get_listings(prices_file_path)
    order_depths = get_order_depths(prices_file_path)
    own_trades = get_trades(trades_file_path)
    market_trades = {}
    position: Dict[Product, Position] = {}
    observations: Dict[Product, Observation] = {}

    state = TradingState(
        timestamp=timestamp,
        listings=listings,
        order_depths=order_depths,
        own_trades=own_trades,
        market_trades=market_trades,
        position=position,
        observations=observations
    )

    return state
    




        



