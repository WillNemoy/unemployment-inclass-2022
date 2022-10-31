
#This is the "app/unemployment_.py" file...
import os
import pandas as pd
from plotly.express import line
from dotenv import load_dotenv # <--- ADDITION

load_dotenv() # <--- ADDITION

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = pd.read_csv(request_url)

print("Get Data:")
print(df.head())
print()

#Challenge A
print("Challenge A:")
print("Latest Unemployment Rate:")
df_first_row = df.iloc[0]
print(f"{df_first_row['timestamp']}:", f"{df_first_row['value']}%")
print()

#Challenge B
print("Challenge B")
df_current_year = df[df["timestamp"].str.contains("2022-")]
print(df_current_year)
print()
print("Average Unemployment this Year:", f"{df_current_year['value'].mean()}%")
print("Number of Months:", len(df_current_year))
print()

#Challenge C
print("Challenge C:")
fig = line(x=df["timestamp"], y=df["value"], title="United States Unemployment Rate Over Time", labels={"x":"Month", "y":"Unemployment Rate"})
fig.show()
