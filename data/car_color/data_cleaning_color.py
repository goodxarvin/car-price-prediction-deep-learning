import pandas as pd
from data.car_color.cleaning_color_funcs import fix_half_space, merge_same_colors




df = pd.read_csv("data/all_cars_data.csv")
df["color"] = df["color"].apply(fix_half_space)
df["color"] = df["color"].apply(merge_same_colors)
df = pd.get_dummies(df, columns=["color"])
df.columns = [col.replace("color_", "") for col in df.columns]


df.to_csv("data/cleaned_color_data.csv", index=False)


