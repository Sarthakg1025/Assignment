# Assignment 48
# Simple Linear Regression - Manual Implementation

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# --------------------------------------------------
# Step 1: Calculate Mean of X
# --------------------------------------------------

mean_x = sum(X) / len(X)

# --------------------------------------------------
# Step 2: Calculate Mean of Y
# --------------------------------------------------

mean_y = sum(Y) / len(Y)

print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)

# --------------------------------------------------
# Step 3: Calculate Slope (m)
#
# m = Σ((X - X_mean)(Y - Y_mean))
#     --------------------------------
#       Σ((X - X_mean)^2)
# --------------------------------------------------

numerator = 0
denominator = 0

for i in range(len(X)):
    numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
    denominator = denominator + ((X[i] - mean_x) ** 2)

m = numerator / denominator

print("Numerator =", numerator)
print("Denominator =", denominator)
print("Slope (m) =", m)

# --------------------------------------------------
# Step 4: Calculate Intercept
#
# c = Y_mean - m * X_mean
# --------------------------------------------------

c = mean_y - (m * mean_x)

print("Intercept (c) =", c)

# --------------------------------------------------
# Step 5: Regression Equation
# --------------------------------------------------

print("\nRegression Equation:")
print("Y =", m, "X +", c)

# --------------------------------------------------
# Step 6: Predict Y values
# --------------------------------------------------

predicted_y = []

print("\nPredicted Y Values:")

for x in X:
    y_pred = (m * x) + c
    predicted_y.append(y_pred)

    print("X =", x, "-> Predicted Y =", y_pred)

# --------------------------------------------------
# Step 7: Predict Y for X = 6
# --------------------------------------------------

x_new = 6

y_new = (m * x_new) + c

print("\nPredicted Y for X = 6:", y_new)