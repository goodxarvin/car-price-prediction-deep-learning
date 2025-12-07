import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error


# تبدیل دوباره از log به قیمت واقعی
y_test_real = np.expm1(y_test)
preds_real = np.expm1(preds)

# محاسبه خطا برای هر نمونه
errors = np.abs(y_test_real - preds_real)

# تبدیل به دیتافریم برای تحلیل راحت‌تر
df_errors = pd.DataFrame({
    "real": y_test_real.flatten(),
    "pred": preds_real.flatten(),
    "error": errors.flatten()
})

# درصد نمونه‌هایی که خطا زیر 50 میلیون دارن
p50 = (df_errors["error"] < 50_000_000).mean() * 100

# درصد نمونه‌هایی که خطا زیر 100 میلیون دارن
p100 = (df_errors["error"] < 100_000_000).mean() * 100

# درصد نمونه‌هایی که خطا زیر 200 میلیون دارن
p200 = (df_errors["error"] < 200_000_000).mean() * 100

print("نمونه‌هایی با خطای کمتر از 50M:", round(p50, 2), "%")
print("نمونه‌هایی با خطای کمتر از 100M:", round(p100, 2), "%")
print("نمونه‌هایی با خطای کمتر از 200M:", round(p200, 2), "%")

# میانگین و میانه خطا
print("\nمیانگین خطا:", int(df_errors["error"].mean()))
print("میانه خطا:", int(df_errors["error"].median()))
