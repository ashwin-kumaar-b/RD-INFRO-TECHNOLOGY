import pandas as pd

# Step 1: Read the CSV
df = pd.read_csv("data.csv")
print("Original Data:")
print(df)

# Step 2: Clean the Data - remove rows with missing values
df_clean = df.dropna()
print("\nCleaned Data:")
print(df_clean)

# Step 3: Write to JSON
df_clean.to_json("output.json", orient="records", indent=4)
print("\nData has been written to output.json")
