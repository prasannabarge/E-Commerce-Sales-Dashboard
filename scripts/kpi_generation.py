import pandas as pd


df = pd.read_csv('../data/cleaned_sales.csv')


# Revenue
df['revenue'] = df['quantity'] * df['unit_price']


# KPIs
kpi = {
'total_revenue': df['revenue'].sum(),
'avg_order_value': df['revenue'].mean(),
'profit_margin': df['profit'].sum() / df['revenue'].sum()
}


print(kpi)