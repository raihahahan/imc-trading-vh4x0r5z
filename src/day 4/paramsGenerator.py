import pandas as pd
import matplotlib.pyplot as plt

# Load the prices CSV file for all three days
prices_day1 = pd.read_csv('csv files/prices_round_4_day_1.csv')
prices_day2 = pd.read_csv('csv files/prices_round_4_day_2.csv')
prices_day3 = pd.read_csv('csv files/prices_round_4_day_3.csv')

# Concatenate the prices dataframes into one
prices = pd.concat([prices_day1, prices_day2, prices_day3])

# Calculate the average mid price for each product
avg_mid_price = prices.groupby('product')['mid_price'].mean()

# Print the average mid price for each product
print('Average mid price for each product:')
print(avg_mid_price)

# Export the average prices to a new CSV file
avg_prices_df = pd.DataFrame({'product': avg_mid_price.index, 'average_prices': avg_mid_price.values})
avg_prices_df.to_csv('day_4_average_prices.csv', index=False)

# Plot the mid price for each product over time
for product in prices['product'].unique():
    product_data = prices[prices['product'] == product]
    plt.plot(product_data['timestamp'], product_data['mid_price'], label=product)

# Add a legend and axis labels to the plot
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Mid Price')
plt.title('Mid Price for each Product over Time')

# Display the plot
plt.show()
