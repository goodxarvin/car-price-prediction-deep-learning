import pandas as pd
from sklearn.preprocessing import LabelEncoder
from data.car_color.cleaning_color_funcs import fix_half_space, merge_same_colors


df = pd.read_csv("data/csv_outputs/all_cars_data.csv")
df = df.dropna(subset="name")
df["color"] = df["color"].apply(fix_half_space)
df["color"] = df["color"].apply(merge_same_colors)


df = pd.get_dummies(df, columns=["color"])
df.columns = [col.replace("color_", "") for col in df.columns]


df.to_csv("data/csv_outputs/cleaned_color_data.csv", index=False)
