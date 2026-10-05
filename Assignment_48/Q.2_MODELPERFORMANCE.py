# ==================================================
# QUESTION 2: MODEL PERFORMANCE
# ==================================================

print("\n" + "=" * 50)
print("QUESTION 2: MODEL PERFORMANCE")
print("=" * 50)

# Dataset
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# Mean of X and Y
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

# Calculate slope (m)
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2

m = numerator / denominator

# Calculate intercept (c)
c = mean_y - (m * mean_x)

# --------------------------------------------------
# Step 1: Predict Y values
# --------------------------------------------------

predicted_y = []

print("\nPredicted Y Values:")
print("-" * 50)

for x in X:
    y_pred = (m * x) + c
    predicted_y.append(y_pred)

    print(
        "X =", x,
        "Actual Y =", Y[x - 1],
        "Predicted Y =", round(y_pred, 2)
    )

# --------------------------------------------------
# Step 2: Calculate MSE
# --------------------------------------------------

sum_squared_error = 0

print("\nIntermediate Calculations:")
print("-" * 60)

print("X\tActual\tPredicted\tError\tSquared Error")

for i in range(len(X)):

    error = Y[i] - predicted_y[i]

    squared_error = error ** 2

    sum_squared_error += squared_error

    print(
        X[i], "\t",
        Y[i], "\t",
        round(predicted_y[i], 2), "\t\t",
        round(error, 2), "\t",
        round(squared_error, 2)
    )

mse = sum_squared_error / len(Y)

print("\nSum of Squared Errors =", round(sum_squared_error, 2))

print("Mean Squared Error (MSE) =", round(mse, 2))

# --------------------------------------------------
# Step 3: Calculate R² Score
# --------------------------------------------------

ss_total = 0

for y in Y:
    ss_total += (y - mean_y) ** 2

r2 = 1 - (sum_squared_error / ss_total)

print("Total Sum of Squares =", round(ss_total, 2))

print("R² Score =", round(r2, 4))