import pandas as pd

#csv
df = pd.read_csv("pokemon.csv")

print(df)
print(df.to_string())

#jason
df = pd.read_json("pokemon.json")

print(df)
print(df.to_string())
