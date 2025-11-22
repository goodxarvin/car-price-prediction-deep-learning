import numpy as np
import pandas as pd
from data.car_name_k_means.data_cleaning_name import kmeans
from sklearn.metrics import silhouette_samples

df = pd.read_csv("data/csv_outputs/cleaned_mileage_model_price_name_color_data.csv")

cluster_sizes = df['name_cluster'].value_counts().sort_values(ascending=False)

print(cluster_sizes)

total_clusters = len(cluster_sizes)
small_under_10 = (cluster_sizes < 10).sum()
small_under_20 = (cluster_sizes < 20).sum()

print("Total clusters =", total_clusters)
print("Clusters with < 10 samples =", small_under_10)
print("Clusters with < 20 samples =", small_under_20)

print("\nPercentage <10 samples = {:.2f}%".format(100 * small_under_10 / total_clusters))
print("Percentage <20 samples = {:.2f}%".format(100 * small_under_20 / total_clusters))

print("\nTop 10 biggest clusters:\n", cluster_sizes.head(10))
print("\nBottom 10 smallest clusters:\n", cluster_sizes.tail(10))
