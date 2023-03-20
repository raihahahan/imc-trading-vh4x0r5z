import pandas as pd
import matplotlib.pyplot as plt

# Read the prices CSV file
prices_df = pd.read_csv('prices.csv', delimiter=';')

# Convert the timestamp column to a datetime object
prices_df['timestamp'] = pd.to_datetime(prices_df['timestamp'], unit='s')

# Create a line chart of the mid_price over time
plt.plot(prices_df['timestamp'], prices_df['mid_price'])
plt.xlabel('Time')
plt.ylabel('Mid Price')
plt.show()
