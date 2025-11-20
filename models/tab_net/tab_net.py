import numpy as np
import pandas as pd
from pytorch_tabnet.tab_model import TabNetRegressor

df = pd.read_csv(
    "data/csv_outputs/cleaned_mileage_model_price_name_color_data.csv.csv")


num_cols = ["mileage", "model"]
cat_cols = ["color_id", "name_cluster"]
selected_cols = cat_cols + num_cols

X = df[selected_cols].values.astype(np.float32)
y = df["price"].values.astype(np.float32).reshape(-1, 1)


cat_idxs = [selected_cols.index(col) for col in cat_cols]
cat_dims = [df[col].nunique() for col in cat_cols]

print(cat_cols, cat_dims)


tabnet_params = {
    "n_d": 8,
    "n_a": 8,
    "n_steps": 5, 
    "gamma": 1.5,
    "cat_idxs": cat_idxs,
    "cat_dims": cat_dims,
    "cat_emb_dim": [4, 8],
    "optimizer_fn": __import__("torch").optim.Adam,
    "optimizer_params": {"lr": 2e-2}
}

model = TabNetRegressor(**tabnet_params)

model.fit(
    X, y,
    max_epochs=100,
    batch_size=256,
    virtual_batch_size=128,
    patience=20,
    drop_last=False
)

preds = model.predict(X)
print(preds[:10])
