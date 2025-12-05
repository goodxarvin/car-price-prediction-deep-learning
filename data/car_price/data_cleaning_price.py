import pandas as pd
import numpy as np

df = pd.read_csv("data/csv_outputs/cleaned_mileage_model_data.csv")
df = df[df["price"] != 39700000000]
df = df[df["price"] != 11111111]
df = df[(df["price"] > 10000000) & (df["price"] < 10000000000)]

df["price_scaled"] = np.log1p(df["price"])

# df["price"] = df["price"].apply(lambda x: x/10000000000)
df.to_csv("data/csv_outputs/cleaned_mileage_model_price_data.csv",
          float_format="%.15f", index=False)
