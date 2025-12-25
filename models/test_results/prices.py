import pandas as pd

df = pd.read_csv("data/csv_outputs/cleaned_mileage_model_price_data.csv")


price_mean = df["price"].mean()
price_min = df["price"].min()
price_max = df["price"].max()
print(price_mean, price_min, price_max)
