import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("input.csv")

# Create a new column for the square rooted shares
df["square rooted shares"] = df["shares"].apply(lambda x: x ** 0.5)

# Create a new column for the difference between the original shares and the square rooted shares
df["difference"] = df["shares"] - df["square rooted shares"]

# Save the DataFrame to a new CSV file
df.to_csv("output.csv", index=False)
