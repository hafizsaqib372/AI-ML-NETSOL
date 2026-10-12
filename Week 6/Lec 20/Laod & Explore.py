import pandas as pd


# 1. Load and Tell pandas the "date" column is a DATE, not text

df = pd.read_csv("shop_sales_daily.csv", parse_dates=['dates'])
print(df.head(3))
print('From', df['date'].min().date(), 'to', df['date'].max().date(),
      '|', len(df), 'days')

# 2. Pull useful parts out of each date

df['dayofweek'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month

# 3. Looks For Patterns

print('\nAverage sales by day of week:')
print(df.groupby('dayofweek')['sales'].mean().round())
print('\nAverage sales by year:')
print(df.groupby(df['dates'].dt.year)['sales'].mean().round())

