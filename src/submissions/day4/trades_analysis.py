import pandas as pd

# Read csv files into dataframes
df1 = pd.read_csv('src\\day4\data\\trades_round_4_day_1_nn.csv', delimiter=';')
df2 = pd.read_csv('src\\day4\data\\trades_round_4_day_2_nn.csv', delimiter=';')
df3 = pd.read_csv('src\\day4\data\\trades_round_4_day_3_nn.csv', delimiter=';')

# Concatenate dataframes into one
df = pd.concat([df1, df2, df3])

# Calculate total quantity and price for each symbol
totals = df.groupby('symbol').agg({'quantity': 'sum', 'price': 'sum'})

print(totals)