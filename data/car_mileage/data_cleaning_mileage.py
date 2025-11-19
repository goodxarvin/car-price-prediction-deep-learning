import pandas as pd

df = pd.read_csv("data/csv_outputs/all_cars_data.csv")

print(df.shape)
df = df.dropna(subset="name")


df["mileage"] = df["mileage"].apply(lambda x: x/999999)
df.to_csv("data/csv_outputs/cleaned_mileage_data.csv",
          index=False, float_format="%.15f")

print(df.shape)