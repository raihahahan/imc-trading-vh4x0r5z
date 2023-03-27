import pandas as pd

# Read csv files into dataframes
df1 = pd.read_csv("src/submissions/day4/data/prices_round_4_day_1.csv", delimiter=';')
df2 = pd.read_csv("src/submissions/day4/data/prices_round_4_day_2.csv", delimiter=';')
df3 = pd.read_csv("src/submissions/day4/data/prices_round_4_day_3.csv", delimiter=';')

# Concatenate dataframes into one
df = pd.concat([df1, df2, df3])

# Calculate mean price for each product
mean_prices = df.groupby('product')['mid_price'].mean()

print(mean_prices)