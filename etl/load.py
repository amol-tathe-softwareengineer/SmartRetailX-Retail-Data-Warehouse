import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:password@localhost/smartretailx")

df = pd.read_csv('../data/processed/clean_sales.csv')

df.to_sql('fact_sales', con=engine, if_exists='append', index=False)

print("Data Loaded Successfully")