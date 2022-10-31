
#This is the "app/unemployment_.py" file...
import os
from pickle import FALSE
import pandas as pd

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = pd.read_csv(request_url)

#print(df.head())

#Challenge A
print("Latest Unemployment Rate:")
df_first_row = df.iloc[0]
print(f"{df_first_row['timestamp']}:", f"{df_first_row['value']}%")