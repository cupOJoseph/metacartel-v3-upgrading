import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("metacartel-v2-hd_Members_1667319488.csv")

# Create a new column for the square rooted shares
df["square rooted shares"] = df["shares"].apply(lambda x: x ** 0.5)

# Create a new column for the difference between the original shares and the square rooted shares
df["difference"] = df["shares"] - df["square rooted shares"]

# Drop the unnecessary columns. The final result must be the format required for generating the moloch v3 dao
df = df.drop(columns=["kicked", "jailed", "tokenTribute", "didRagequit", "exists", "createdAt", "isDao", "isSafeMinion", "delegateKey", "shares", "loot"])

# Save the DataFrame to a new CSV file
df.to_csv("moloch-v3-output.csv", index=False)
