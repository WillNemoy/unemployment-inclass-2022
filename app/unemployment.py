
#This is the "app/unemployment_.py" file...
import os
import pandas as pd

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = pd.read_csv(request_url)

print(df.head())
print(df.columns)
print(len(df))