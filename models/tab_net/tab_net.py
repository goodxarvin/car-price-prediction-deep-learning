import numpy as np
import pandas as pd
import torch
from torch import nn
from pytorch_tabnet.tab_model import TabNetRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


print(torch.cuda.is_available())
# print(torch.cuda.get_device_name())


df = pd.read_csv(
    "data/csv_outputs/cleaned_mileage_model_price_name_color_data.csv")

df = df.sample(frac=1, random_state=42).reset_index(drop=True)


num_cols = ["mileage", "model"]
# cat_cols = ["model_id", "color_id", "name_cluster"]
cat_cols = ["color_id", "name_cluster"]

selected_cols = cat_cols + num_cols

X = df[selected_cols].values.astype(np.float32)
y = df["price_scaled"].values.astype(np.float32).reshape(-1, 1)

cat_idxs = [selected_cols.index(col) for col in cat_cols]
cat_dims = [df[col].nunique() for col in cat_cols]


X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)


X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.15, random_state=42)

# print(cat_cols, cat_dims)

print(f"cluster names: {df['name_cluster'].nunique()}")
print(f"train size: {X_train.shape[0]}")
print(f"validation size: {X_val.shape[0]}")
print(f"test size: {X_test.shape[0]}")


car_cluster_dims = [y for y in range(4, 64)]
mse_results = {}
mae_results = {}
# device = torch.device("cpu")


tabnet_params = {
    "n_d": 14,
    "n_a": 11,
    "n_steps": 8,
    "gamma": 0.9,
    "cat_idxs": cat_idxs,
    "cat_dims": cat_dims,
    "cat_emb_dim": [4, 15],
    "optimizer_fn": __import__("torch").optim.Adam,
    "optimizer_params": {"lr": 2e-2},
    "mask_type": "sparsemax",
    "momentum": 0.1,
}

model = TabNetRegressor(**tabnet_params)

model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    max_epochs=100,
    loss_fn=nn.SmoothL1Loss(),
    batch_size=64,
    virtual_batch_size=32,
    patience=15,
    drop_last=False
)

preds = model.predict(X_test)

real_preds = np.expm1(preds)
y_test_real = np.expm1(y_test)

X_test_df = pd.DataFrame(X_test, columns=selected_cols)

results_df = pd.DataFrame({
    "mileage": X_test_df["mileage"],
    "model": X_test_df["model"],
    "color_id": X_test_df["color_id"],
    "name_cluster": X_test_df["name_cluster"],
    "real": y_test_real.flatten(),
    "pred": real_preds.flatten(),
})

results_df["error"] = np.abs(results_df["real"] - results_df["pred"])

results_df.to_csv("error_analysis/results.csv", index=False)

mse = mean_squared_error(y_test_real, real_preds)
mae = mean_absolute_error(y_test_real, real_preds)

print("MSE:", round(float(mse), 6))
print("MAE:", round(float(mae), 6))


# with open("models/tab_net/results.txt", "a", encoding="utf-8") as file:
#     file.write(f"k={df['name_cluster'].nunique()}\n")
#     file.write(
#         f"best mse at {min(mse_results.keys())} at car embed {mse_results[min(mse_results.keys())]}\n")
#     file.write(
#         f"best mae at {min(mae_results.keys())} at car embed {mae_results[min(mae_results.keys())]}\n")


# for real, pred in zip(y_test[:10], preds[:10]):
#     print("Actual:    {:.1f}\nPredicted: {:.1f}\n".format(
#         float(real[0].item())*35000000000, abs(float(pred)*35000000000)))

# print()
