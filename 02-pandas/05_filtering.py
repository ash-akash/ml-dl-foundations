# filtering = keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("pokemon.csv")

# tall_pokemon = df[df["Height"]>2]
# print(tall_pokemon)

heavy_pokemon = df[df["Weight"]>100]
print(heavy_pokemon)

