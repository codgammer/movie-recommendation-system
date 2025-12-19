import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

ratings = pd.read_csv("data/ratings.csv")

actual = ratings["rating"]
predicted = np.random.uniform(3, 5, size=len(actual))

rmse = np.sqrt(mean_squared_error(actual, predicted))
mae = mean_absolute_error(actual, predicted)

print("RMSE:", rmse)
print("MAE:", mae)

ratings["rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Rating Distribution")
plt.savefig("rating_distribution.png")
plt.close()

plt.bar(["RMSE", "MAE"], [rmse, mae])
plt.title("Accuracy Metrics")
plt.savefig("accuracy_metrics.png")
plt.close()
