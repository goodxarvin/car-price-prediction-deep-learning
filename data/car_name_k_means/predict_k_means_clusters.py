import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/csv_outputs/cleaned_mileage_model_price_name_color_data.csv")

names = df['name'].astype(str).tolist()

vectorizer = TfidfVectorizer(min_df=5)
X = vectorizer.fit_transform(names)


sse = []
K_range = range(700, 701)

for k in K_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    sse.append(km.inertia_)

plt.plot(K_range, sse, marker='o')
plt.xlabel("k")
plt.ylabel("SSE")
plt.title("Elbow Method")
plt.show()


sil_scores = []

for i, k in enumerate(K_range):
    print(f"loop {i+1}")
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(X)
    score = silhouette_score(X, labels)
    sil_scores.append(score)

plt.plot(K_range, sil_scores, marker='o')
plt.xlabel("k")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Analysis")
plt.show()


best_k = K_range[sil_scores.index(max(sil_scores))]
print("Best k =", best_k)
