import numpy as np
import pandas as pd
<<<<<<< HEAD
import torch.nn as nn
=======
>>>>>>> dbf2b767c64db9bcfa92cb6439c677028afbc7b0
import torch
from pytorch_tabnet.tab_model import TabNetRegressor
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error


print(torch.cuda.is_available())
# print(torch.cuda.get_device_name())


df = pd.read_csv(
    "data/csv_outputs/cleaned_mileage_model_price_name_color_data.csv")

df = df.sample(frac=1, random_state=42).reset_index(drop=True)


num_cols = ["mileage", "model"]
cat_cols = ["color_id", "name_cluster"]
selected_cols = cat_cols + num_cols

X = df[selected_cols].values.astype(np.float32)
y = df["price"].values.astype(np.float32).reshape(-1, 1)


kf = KFold(n_splits=5, shuffle=True, random_state=42)


cat_idxs = [selected_cols.index(col) for col in cat_cols]
cat_dims = [df[col].nunique() for col in cat_cols]


# X_temp, X_test, y_temp, y_test = train_test_split(
#     X, y, test_size=0.1, random_state=42)


X_train_full, X_test, y_train_full, y_test = train_test_split(
<<<<<<< HEAD
    X, y, test_size=0.1, random_state=42)
=======
    X, y, test_size=0.15, random_state=42)
>>>>>>> dbf2b767c64db9bcfa92cb6439c677028afbc7b0

# print(cat_cols, cat_dims)
# print(f"train size: {X_train.shape[0]}")
# print(f"validation size: {X_val.shape[0]}")
# print(f"test size: {X_test.shape[0]}")


tabnet_params = {
    "n_d": 22,
    "n_a": 16,
    "n_steps": 8,
    "gamma": 0.7,
    "cat_idxs": cat_idxs,
    "cat_dims": cat_dims,
    "cat_emb_dim": [4, 12],
    "optimizer_fn": __import__("torch").optim.Adam,
    "optimizer_params": {"lr": 2e-2}
}

fold_mse = []
fold_mae = []

for fold, (train_idx, val_idx) in enumerate(kf.split(X_train_full)):
    print(f"fold: {fold}")
    X_train, X_val = X_train_full[train_idx], X_train_full[val_idx]
    y_train, y_val = y_train_full[train_idx], y_train_full[val_idx]

    model = TabNetRegressor(**tabnet_params)
    model.fit(
        X_train, y_train,
        eval_set=[(X_val, y_val)],
        loss_fn=nn.SmoothL1Loss(),
        max_epochs=100,
        batch_size=128,
        virtual_batch_size=64,
        patience=15,
        drop_last=False
    )

    preds = model.predict(X_val).flatten()
    real = y_val.flatten()

    mse = ((preds - real)**2).mean()
    mae = np.abs(preds - real).mean()

    fold_mse.append(mse)
    fold_mae.append(mae)

    print(f"fold {fold} mse: {round(mse, 6)}")
    print(f"fold {fold} mae: {round(mae, 6)}")


print(f"final mse: {np.mean(fold_mse)}")
print(f"final mae: {np.mean(fold_mae)}")

test_prediction = model.predict(X_test)

<<<<<<< HEAD
mse_test = mean_squared_error(y_test, test_prediction)
mae_test = mean_absolute_error(y_test, test_prediction)

print("test MSE:", round(float(mse_test), 6))
print("test MAE:", round(float(mae_test), 6), round(float(mae), 6)*35000000000)
=======
mse_test = mean_squared_error(y_test, preds)
mae_test = mean_absolute_error(y_test, preds)

print("MSE:", round(float(mse_test), 6))
print("MAE:", round(float(mae_test), 6), round(float(mae), 6)*35000000000)
>>>>>>> dbf2b767c64db9bcfa92cb6439c677028afbc7b0


# for real, pred in zip(y_test[:10], preds[:10]):
#     print("Actual:    {:.1f}\nPredicted: {:.1f}\n".format(
#         float(real[0].item())*35000000000, abs(float(pred)*35000000000)))
