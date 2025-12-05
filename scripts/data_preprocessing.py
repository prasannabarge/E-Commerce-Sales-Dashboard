import pandas as pd


sales = pd.read_csv('../data/sales_data.csv')
customers = pd.read_csv('../data/customers.csv')


# Merge datasets
df = sales.merge(customers, on='customer_id', how='left')


# Convert date
df['order_date'] = pd.to_datetime(df['order_date'])


# Save
df.to_csv('../data/cleaned_sales.csv', index=False)