import pandas as pd
import os

files = os.listdir("data")
dfs = [pd.read_csv(f"data/{file}") for file in files]

# Combine into one dataframe
df = pd.concat(dfs)

# Filter for Pink Morsels only
df = df[df["product"] == "pink morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Save result
df.to_csv("formatted_sales.csv", index=False)

print("Output saved as formatted_sales.csv")