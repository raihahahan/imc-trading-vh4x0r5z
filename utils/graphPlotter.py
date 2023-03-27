import pandas as pd
import matplotlib.pyplot as plt

# # Read the prices CSV file
# prices_df = pd.read_csv('utils\data\prices_round_4_day_1.csv', delimiter=';')

# # Convert the timestamp column to a datetime object
# prices_df['timestamp'] = pd.to_datetime(prices_df['timestamp'], unit='s')

# # Create a line chart of the mid_price over time
# plt.plot(prices_df['timestamp'], prices_df['mid_price'])
# plt.xlabel('Time')
# plt.ylabel('Mid Price')
# plt.show()

CSV_PATH = ""
# Read the prices CSV file
prices_df = pd.read_csv(CSV_PATH, delimiter=';')

# Convert the timestamp column to a datetime object
prices_df['timestamp'] = pd.to_datetime(prices_df['timestamp'], unit='ms')

# Create a line chart of the mid_price over time
plt.plot(prices_df['timestamp'], prices_df['price'])
plt.plot(prices_df['timestamp'], prices_df['quantity'])
plt.xlabel('Time')
plt.ylabel('Mid Price')
plt.show()
