import numpy as np

from sklearn.linear_model import LinearRegression


# Step 1: Create dataset
X = np.array([[1],
              [2],
              [3],
              [4],
              [5]])

Y = np.array([50, 55, 60, 65, 70])

# Step 2: Create regression model
model = LinearRegression()

# Step 3: Train the model
model.fit(X, Y)

# Step 4: Display coefficient
print("Coefficient :", model.coef_[0])

# Step 5: Display intercept
print("Intercept :", model.intercept_)