import numpy as np
import pandas as pd

df_errors = pd.read_csv("error_analysis/results.csv")

y_test_real = df_errors["real"]
real_preds = df_errors["preds"]

errors = np.abs(y_test_real - real_preds)


p50 = (df_errors["error"] < 50_000_000).mean() * 100

p100 = (df_errors["error"] < 100_000_000).mean() * 100

p200 = (df_errors["error"] < 200_000_000).mean() * 100

print("less then 50M", round(p50, 2), "%")
print("less then 100M:", round(p100, 2), "%")
print("less then 200M", round(p200, 2), "%")

print("\nloss mean", int(df_errors["error"].mean()))
print("loss middle", int(df_errors["error"].median()))


threshold = df_errors["error"].quantile(0.95)
bad_cases = df_errors[df_errors["error"] >= threshold]

print("worst data:", len(bad_cases))
print(bad_cases.head(10))
