import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

ratings = pd.read_csv("data/ratings.csv")

actual = ratings["rating"]
predicted = np.random.uniform(3, 5, size=len(actual))

rmse = np.sqrt(mean_squared_error(actual, predicted))
mae = mean_absolute_error(actual, predicted)

print("RMSE:", rmse)
print("MAE:", mae)

ratings["rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Rating Distribution")
plt.show()

plt.bar(["RMSE", "MAE"], [rmse, mae])
plt.title("Accuracy Metrics")
plt.show()