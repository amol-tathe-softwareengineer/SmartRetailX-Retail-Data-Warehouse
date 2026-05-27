import pandas as pd

customers = pd.read_csv('../data/raw/customers.csv')
products = pd.read_csv('../data/raw/products.csv')
sales = pd.read_csv('../data/raw/sales.csv')

print("Data Extracted Successfully")