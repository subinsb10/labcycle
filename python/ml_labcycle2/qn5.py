import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Given data
X = np.array([2, 4, 6, 8, 10, 12]).reshape(-1, 1)  # Advertising Spend (in $1000s)
y = np.array([4.1, 7.2, 9.8, 13.2, 15.4, 18.1])   # Sales Revenue (in $1000s)

# a) Scatter plot of data points
plt.scatter(X, y, color='blue', label='Data Points')

# b) Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# c) Calculate slope (b1) and intercept (b0)
slope = model.coef_[0]
intercept = model.intercept_
print(f"Slope (b1): {slope:.2f}")
print(f"Intercept (b0): {intercept:.2f}")

# d) Plot regression line
y_pred = model.predict(X)
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.xlabel('Advertising Spend ($1000s)')
plt.ylabel('Sales Revenue ($1000s)')
plt.title('Advertising Spend vs Sales Revenue')
plt.legend()
plt.grid(True)
plt.show()

# e) Predict sales when advertising spend is $9,000
prediction_9k = model.predict(np.array([[9]]))[0]
print(f"Predicted Sales Revenue at $9k spend: {prediction_9k:.2f} ($1000s)")

# f) Calculate R² and MSE
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
print(f"R-squared (R²): {r2:.3f}")
print(f"Mean Squared Error (MSE): {mse:.3f}")
