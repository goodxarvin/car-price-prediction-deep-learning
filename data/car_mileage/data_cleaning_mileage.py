import pandas as pd
from data.car_mileage.cleaning_mileage_funcs import normalize

df = pd.read_csv("data/cleaned_color_data.csv")
df["mileage"] = df["mileage"].apply(normalize)
df.to_csv("data/cleaned_color_mileage_data.csv", index=False)