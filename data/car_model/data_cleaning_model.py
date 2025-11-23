import pandas as pd
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("data/csv_outputs/cleaned_mileage_data.csv")
df["model"] = df["model"].apply(lambda x: x-621 if x > 1950 else x)
df["model"] = df["model"].apply(lambda x: x/1404)


model_encoder = LabelEncoder()
df["model_id"] = model_encoder.fit_transform(df["model"])

# df = pd.get_dummies(df, columns=["model"])
# df.columns = [col.replace("model_", "") for col in df.columns]


df.to_csv("data/csv_outputs/cleaned_mileage_model_data.csv",
          index=False, float_format="%.15f")
