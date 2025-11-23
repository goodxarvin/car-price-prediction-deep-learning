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
y = df["price"].values.astype(np.float32).reshape(-1, 1)

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


tabnet_params = {
    "n_d": 32,
    "n_a": 32,
    "n_steps": 8,
    "gamma": 0.7,
    "cat_idxs": cat_idxs,
    "cat_dims": cat_dims,
    "cat_emb_dim": [4, 24],
    "optimizer_fn": __import__("torch").optim.Adam,
    "optimizer_params": {"lr": 2e-2},
    "mask_type": "entmax"
}

model = TabNetRegressor(**tabnet_params)

model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    max_epochs=100,
    loss_fn=nn.SmoothL1Loss(),
    batch_size=128,
    virtual_batch_size=64,
    patience=15,
    drop_last=False
)

preds = model.predict(X_test)

mse = mean_squared_error(y_test, preds)
mae = mean_absolute_error(y_test, preds)

print("MSE:", round(float(mse), 6))
print("MAE:", round(float(mae), 6), round(float(mae), 6)*35000000000)


for real, pred in zip(y_test[:10], preds[:10]):
    print("Actual:    {:.1f}\nPredicted: {:.1f}\n".format(
        float(real[0].item())*35000000000, abs(float(pred)*35000000000)))
