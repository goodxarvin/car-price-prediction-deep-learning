import pandas as pd
from data.car_model.cleaning_model_funcs import convert_year, normalize

df = pd.read_csv("data/csv_outputs/cleaned_color_mileage_data.csv")
df["model"] = df["model"].apply(convert_year)
df = pd.get_dummies(df, columns=["model"])
df.columns = [col.replace("model_", "") for col in df.columns]
df.to_csv("data/csv_outputs/cleaned_color_mileage_model_data.csv", index=False)

