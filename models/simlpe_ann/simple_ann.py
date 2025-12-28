from sklearn.metrics import mean_absolute_error
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Flatten, Concatenate
import pandas as pd
import os
import random

SEED = 42

os.environ["PYTHONHASHSEED"] = str(SEED)
os.environ["TF_DETERMINISTIC_OPS"] = "1"

random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)


df = pd.read_csv(
    "data/csv_outputs/cleaned_mileage_model_price_name_color_data.csv")

features = ["model", "mileage", "color_id", "name_cluster"]
target = "price_scaled"

X = df[features]
y = df[target]

X["color_id"] = X["color_id"].astype("int32")
X["name_cluster"] = X["name_cluster"].astype("int32")

X["model"] = X["model"].astype("float32")
X["mileage"] = X["mileage"].astype("float32")
y = y.astype("float32")

X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)


X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.15, random_state=42)


num_colors = X["color_id"].nunique()
num_names = X["name_cluster"].nunique()
print(f"colors: {num_colors}", f"names: {num_names}")

model_in = Input(shape=(1,), name="model")
mileage_in = Input(shape=(1,), name="mileage")

color_in = Input(shape=(1,), name="color_id")
name_in = Input(shape=(1,), name="name_cluster")

color_emb = Embedding(
    input_dim=num_colors + 1,
    output_dim=4
)(color_in)

name_emb = Embedding(
    input_dim=num_names + 1,
    output_dim=16
)(name_in)


color_emb = Flatten()(color_emb)
name_emb = Flatten()(name_emb)

x = Concatenate()([
    model_in,
    mileage_in,
    color_emb,
    name_emb
])

x = Dense(256, activation="relu")(x)
x = Dense(128, activation="relu")(x)
x = Dense(64, activation="relu")(x)
x = Dense(32, activation="relu")(x)

output = Dense(1)(x)


model = Model(
    inputs=[model_in, mileage_in, color_in, name_in],
    outputs=output
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="huber",
    metrics=["mae", "mse"]
)

model.summary()


history = model.fit(
    {
        "model": X_train["model"],
        "mileage": X_train["mileage"],
        "color_id": X_train["color_id"],
        "name_cluster": X_train["name_cluster"]
    },
    y_train,
    validation_data=(
        {
            "model": X_val["model"],
            "mileage": X_val["mileage"],
            "color_id": X_val["color_id"],
            "name_cluster": X_val["name_cluster"]
        },
        y_val
    ),
    epochs=85,
    batch_size=256,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            patience=5,
            restore_best_weights=True
        )
    ]
)


y_pred_log = model.predict({
    "model": X_val["model"],
    "mileage": X_val["mileage"],
    "color_id": X_val["color_id"],
    "name_cluster": X_val["name_cluster"]
})

y_pred_price = np.exp(y_pred_log)
y_true_price = np.exp(y_val)


mae_real = mean_absolute_error(y_true_price, y_pred_price)
print("Real MAE (Toman):", mae_real)
