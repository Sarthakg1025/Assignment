from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Create input features
X = np.array([
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
])

# Step 2: Create target values
Y = np.array([50, 55, 60, 65, 70])

# Step 3: Create regression model
model = LinearRegression()

# Step 4: Train the model
model.fit(X, Y)

# Step 5: Print coefficients
print("Coefficient for StudyHours :", model.coef_[0])
print("Coefficient for SleepHours :", model.coef_[1])

# Step 6: Print intercept
print("Intercept :", model.intercept_)