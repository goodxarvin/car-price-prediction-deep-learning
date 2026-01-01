import pandas as pd
from data.car_name_k_means.cleaning_name_funcs import filter_unuseful_words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


df = pd.read_csv("data/csv_outputs/cleaned_mileage_model_price_data.csv")
df["name"] = df["name"].apply(filter_unuseful_words)
print("before accident: ", len(df))
df = df[~df["name"].str.contains("تصادفی", na=False)]
print("after accident: ", len(df), "\n")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["name"])

kmeans = KMeans(n_clusters=590, random_state=42)
df["name_cluster"] = kmeans.fit_predict(X)

with open("data/car_name_k_means/cluster.txt", "w", encoding="utf-8") as file:
    for i in range(kmeans.n_clusters):
        file.write(f"\n--- cluster {i} ---\n")
        file.write(df[df['name_cluster'] == i]
                   ['name'].head(10).to_string(index=False))
        file.write("\n")




clean_rows = []

for cluster_id, group in df.groupby("name_cluster"):

    q1 = group["price"].quantile(0.3)
    q3 = group["price"].quantile(0.7)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    good = group[(group["price"] >= lower) &
                 (group["price"] <= upper)]

    clean_rows.append(good)

df_clean = pd.concat(clean_rows, ignore_index=True)


print("before cleaning: ", len(df))
print("after cleaning: ", len(df_clean))
print("number deleted: ", len(df) - len(df_clean))


df_clean.to_csv("data/csv_outputs/cleaned_mileage_model_price_name_data.csv",
                float_format="%.15f", index=False)


# name_cluster_dummies = pd.get_dummies(df["name_cluster"])
# df = pd.concat([df, name_cluster_dummies], axis=1)
# nan_name = df[df["name"].isna()]
# nan_color = df[df["color"].isna()]
# nan_model = df[df["model"].isna()]
# nan_mileage = df[df["mileage"].isna()]
# nan_price = df[df["price"].isna()]
# print(nan_name, nan_mileage, nan_price)
