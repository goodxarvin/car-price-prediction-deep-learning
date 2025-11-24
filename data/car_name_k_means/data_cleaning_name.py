import pandas as pd
from hazm import word_tokenize
from data.car_name_k_means.cleaning_name_funcs import filter_unuseful_words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


df = pd.read_csv("data/csv_outputs/cleaned_mileage_model_price_data.csv")
# print(df["name"][1])
df["name"] = df["name"].apply(filter_unuseful_words)
# print(df["name"][1])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["name"])

kmeans = KMeans(n_clusters=800, random_state=42)
df["name_cluster"] = kmeans.fit_predict(X)


with open("cluster.txt", "w", encoding="utf-8") as file:
    for i in range(kmeans.n_clusters):
        file.write(f"\n--- خوشه {i} ---\n")
        file.write(df[df['name_cluster'] == i]
                   ['name'].head(10).to_string(index=False))
        file.write("\n")


df.to_csv("data/csv_outputs/cleaned_mileage_model_price_name_data.csv",
          float_format="%.15f", index=False)

print(df.shape)

# name_cluster_dummies = pd.get_dummies(df["name_cluster"])
# df = pd.concat([df, name_cluster_dummies], axis=1)
# nan_name = df[df["name"].isna()]
# nan_color = df[df["color"].isna()]
# nan_model = df[df["model"].isna()]
# nan_mileage = df[df["mileage"].isna()]
# nan_price = df[df["price"].isna()]
# print(nan_name, nan_mileage, nan_price)
