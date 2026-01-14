import pandas as pd

df = pd.read_csv("pokemon.csv", index_col = "Name")

# SELECTION by column

print(df["Name"].to_string())
print(df["Height"].to_string())
print(df["Weight"].to_string())
print(df[["Name","Height","Weight"]])

# Selection by rows
print(df.loc["Pikachu", ["Height", "Weight"]])
print(df.iloc[0:11])