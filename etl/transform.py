import pandas as pd

sales = pd.read_csv('../data/raw/sales.csv')

sales.dropna(inplace=True)

sales['total_amount'] = sales['quantity'] * sales['price']

sales.to_csv('../data/processed/clean_sales.csv', index=False)

print("Transformation Completed")