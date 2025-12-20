import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_errors = pd.read_csv("error_analysis/results.csv")

y_test_real = df_errors["real"]
real_preds = df_errors["pred"]

errors = np.abs(y_test_real - real_preds)


p50 = (df_errors["error"] < 50_000_000).mean() * 100

p100 = (df_errors["error"] < 100_000_000).mean() * 100

p200 = (df_errors["error"] < 200_000_000).mean() * 100

print("less then 50M:", round(p50, 2), "%")
print("less then 100M:", round(p100, 2), "%")
print("less then 200M:", round(p200, 2), "%")

print("\nloss mean", int(df_errors["error"].mean()))
print("loss middle", int(df_errors["error"].median()))


threshold = df_errors["error"].quantile(0.95)
bad_cases = df_errors[df_errors["error"] >= threshold]


worst_samples = df_errors.sort_values("error", ascending=False).head(10)
print(worst_samples)


print("worst data:", len(bad_cases))
print(bad_cases.head(10))


plt.figure(figsize=(10, 6))
plt.hist(df_errors["error"]/1e6, bins=50)
plt.xlabel("loss (million toman)")
plt.ylabel("sample number")
plt.title("scattering")
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(df_errors["real"]/1e6, df_errors["error"]/1e6, alpha=0.5)
plt.xlabel("real pprice (million toman)")
plt.ylabel("loss (million toman)")
plt.title("relation between loss and real prices")
plt.show()


plt.figure(figsize=(12, 6))
sns.boxplot(x="name_cluster", y="error", data=df_errors)
plt.ylim(0, 2e9)
plt.title("loss by (name cluster)")
plt.show()
