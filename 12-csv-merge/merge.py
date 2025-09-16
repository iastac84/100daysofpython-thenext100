import pandas as pd

# Read the CSV files
df_a = pd.read_csv("file_a.csv")
df_b = pd.read_csv("file_b.csv")

# Merge the files on the 'name' column
merged = pd.merge(df_a, df_b, on="name", how="inner")  # use "outer", "left", or "right" as needed

# Save to a new CSV
merged.to_csv("merged.csv", index=False)
