from datamodel import *

def run(state: TradingState):
        #    Initialize the method output dict as an empty dict
        result = {}

        # Iterate over all the keys (the available products) contained in the order depths
        for product in state.order_depths.keys():

            # Check if the current product is the 'PEARLS' product, only then run the order logic
            if product == 'PEARLS':

                # Retrieve the Order Depth containing all the market BUY and SELL orders for PEARLS
                order_depth: OrderDepth = state.order_depths[product]

                # Initialize the list of Orders to be sent as an empty list
                orders: list[Order] = []

                # Define a fair value for the PEARLS.
                # Note that this value of 1 is just a dummy value, you should likely change it!
                acceptable_price = 123123

                # If statement checks if there are any SELL orders in the PEARLS market
                if len(order_depth.sell_orders) > 0:

                    # Sort all the available sell orders by their price,
                    # and select only the sell order with the lowest price
                    best_ask = min(order_depth.sell_orders.keys())
                    best_ask_volume = order_depth.sell_orders[best_ask]

                    # Check if the lowest ask (sell order) is lower than the above defined fair value
                    if best_ask < acceptable_price:

                        # In case the lowest ask is lower than our fair value,
                        # This presents an opportunity for us to buy cheaply
                        # The code below therefore sends a BUY order at the price level of the ask,
                        # with the same quantity
                        # We expect this order to trade with the sell order
                        order("BUY", product=product, price=best_ask, volume=best_ask_volume, state=state, orders=orders)

                # The below code block is similar to the one above,
                # the difference is that it finds the highest bid (buy order)
                # If the price of the order is higher than the fair value
                # This is an opportunity to sell at a premium
                if len(order_depth.buy_orders) != 0:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_bid_volume = order_depth.buy_orders[best_bid]
                    if best_bid > acceptable_price:
                        order("SELL", product=product, price=best_bid, volume=best_bid_volume, state=state, orders=orders)

                # Add all the above orders to the result dict
                result[product] = orders

                # Return the dict of orders
                # These possibly contain buy or sell orders for PEARLS
                # Depending on the logic above
        return result


        
#     def _run(state: TradingState) -> Dict[str, List[Order]]:
#         global prices
#         prices = []
#         result = {}

#         # showTrades(state) 
#         for product in state.position.keys():
#             print(f"position: {product} {state.position[product]}")
            

#         for product in state.order_depths.keys():
#             if product == 'BANANAS': 
#                 inventory = 0
#                 if product in state.position.keys():
#                     inventory = state.position[product]
#                 order_depth = state.order_depths[product]
#                 orders = []

#                 if len(order_depth.sell_orders) > 0 and len(order_depth.buy_orders) > 0:
#                     best_ask = min(order_depth.sell_orders.keys())
#                     best_ask_volume = order_depth.sell_orders[best_ask]
#                     best_bid = max(order_depth.buy_orders.keys())
#                     best_bid_volume = order_depth.buy_orders[best_bid]
#                     spread = best_ask - best_bid
                    
#                 ##design orders in 
#                 # {low premium: + high volume, high premium: + low volume} 
#                 # {high discount: - low volume, low discount: - high volume}
#                     premium_interval = [0.1, 0.4, 0.6, 0.9]
#                     resting_prices = [round(p * spread+best_bid) for p in premium_interval]
#                     volume_scaler = [0.7, 0.3, -0.3, -0.7]
#                     resting_volumes = [round(0.7*(20-inventory)), round(0.3*(20-inventory)), 
#                                        round(-0.3*(20+inventory)), round(-0.7*(20+inventory))]

#                     orders = sendOrders(product, resting_prices, resting_volumes)
#                     result[product] = orders  
                


#             if product == 'PEARLS': 
#                 inventory = 0
#                 if product in state.position.keys():
#                     inventory = state.position[product]
#                 order_depth = state.order_depths[product]
#                 orders = []

#                 if len(order_depth.sell_orders) > 0 and len(order_depth.buy_orders) > 0:
#                     best_ask = min(order_depth.sell_orders.keys())
#                     best_ask_volume = order_depth.sell_orders[best_ask]
#                     best_bid = max(order_depth.buy_orders.keys())
#                     best_bid_volume = order_depth.buy_orders[best_bid]
#                     spread = best_ask - best_bid
                    
#                 ##design orders in 
#                 # {low premium: + high volume, high premium: + low volume} 
#                 # {high discount: - low volume, low discount: - high volume}
#                     premium_interval = [0.1, 0.4, 0.6, 0.9]
#                     resting_prices = [round(p * spread+best_bid) for p in premium_interval]
#                     volume_scaler = [0.7, 0.3, -0.3, -0.7]
#                     resting_volumes = [round(0.7*(20-inventory)), round(0.3*(20-inventory)), 
#                                        round(-0.3*(20+inventory)), round(-0.7*(20+inventory))]

#                     orders = sendOrders(product, resting_prices, resting_volumes)
#                     result[product] = orders  

#         print("="*50)
#         return result
           
# ###take a list of prices, volumes of a product into orders
#     def sendOrders(product, prices, volumes):
#         orders = []
#         for i in range(len(prices)):
#             order = Order(product, prices[i], volumes[i])
#             print(order)
#             orders.append(order)
#         return orders
        
# ###show trades method to be called in Trade::run()
#     def showTrades(state: TradingState) :  
#         print("")  
#         for product in ["BANANAS", "PEARLS"]:
#             if product in state.market_trades:
#                 tradeLst = state.market_trades[product]
#                 for i in range(len(tradeLst)):
#                     price = tradeLst[i].price
#                     volume = tradeLst[i].quantity
#                     print(f"{volume} of {product} traded @ {price}")
            
#             if product in state.own_trades:
#                 tradeLst = state.own_trades[product]
#                 for i in range(len(tradeLst)):
#                     price = tradeLst[i].price
#                     volume = tradeLst[i].quantity
#                     if tradeLst[i].buyer == "SUBMISSION":
#                         print(f"{volume} of {product} traded @ {price} (SELF BUY)")  
#                     else:
#                         print(f"{volume} of {product} traded @ {price} (SELF SELL)") 
#     return _run(state)

def order(type: str, product: str, price: int, volume: int, state: TradingState, orders: list[Order]):
    print(product, ":", type, str(-volume) + "x", price)
    if type == "BUY":
        state.order_depths[product].sell_orders.pop(price)
    elif type == "SELL":
        state.order_depths[product].buy_orders.pop(price)

    orders.append(Order(product, price, -volume))

    
     