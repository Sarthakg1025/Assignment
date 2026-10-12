# ==================================================
# QUESTION 3: SALARY PREDICTION
# ==================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --------------------------------------------------
# Step 1: Create Dataset
# --------------------------------------------------

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

Y = np.array([20000, 25000, 30000, 35000, 40000])

print("Experience:")
print(X.flatten())

print("\nSalary:")
print(Y)

# --------------------------------------------------
# Step 2: Create Linear Regression Model
# --------------------------------------------------

model = LinearRegression()

# --------------------------------------------------
# Step 3: Train Model
# --------------------------------------------------

model.fit(X, Y)

print("\nModel Training Completed Successfully!")

# --------------------------------------------------
# Step 4: Display Slope and Intercept
# --------------------------------------------------

m = model.coef_[0]
c = model.intercept_

print("\nSlope (m) =", m)
print("Intercept (c) =", c)

print("\nRegression Equation:")
print("Salary =", m, "* Experience +", c)

# --------------------------------------------------
# Step 5: Predict Salary for 6 Years Experience
# --------------------------------------------------

new_experience = np.array([[6]])

predicted_salary = model.predict(new_experience)

print(
    "\nPredicted Salary for 6 Years Experience: ₹",
    int(predicted_salary[0])
)

# --------------------------------------------------
# Step 6: Predict Salary for Existing Data
# --------------------------------------------------

predicted_values = model.predict(X)

print("\nSalary Predictions:")
print("-" * 50)

for i in range(len(X)):
    print(
        "Experience:", X[i][0], "Years",
        "| Actual Salary: ₹", Y[i],
        "| Predicted Salary: ₹", int(predicted_values[i])
    )

# --------------------------------------------------
# Step 7: Plot Data Points
# --------------------------------------------------

plt.scatter(
    X,
    Y,
    label="Data Points"
)

# --------------------------------------------------
# Step 8: Plot Regression Line
# --------------------------------------------------

plt.plot(
    X,
    predicted_values,
    label="Regression Line"
)

# --------------------------------------------------
# Step 9: Add Labels and Title
# --------------------------------------------------

plt.xlabel("Experience (Years)")
plt.ylabel("Salary (₹)")

plt.title("Experience vs Salary - Linear Regression")

plt.legend()
plt.grid(True)

# --------------------------------------------------
# Step 10: Display Graph
# --------------------------------------------------

plt.show()