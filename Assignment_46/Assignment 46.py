# Assignment 46
# Advertising Sales Prediction using Linear Regression

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ---------------------------------------------------------
# Step 1 : Get Data
# ---------------------------------------------------------

print("Step 1 : Getting Data")

df = pd.read_csv("Advertising.csv")

print("Dataset:")
print(df.head())

# ---------------------------------------------------------
# Step 2 : Clean, Prepare and Manipulate Data
# ---------------------------------------------------------

print("\nStep 2 : Clean, Prepare and Manipulate Data")

# Remove unnecessary index column
df = df.drop("Unnamed: 0", axis=1)

print("\nDataset after removing unnecessary column:")
print(df.head())

# Features
X = df[["TV", "radio", "newspaper"]]

# Target
Y = df["sales"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(Y.head())

# ---------------------------------------------------------
# Step 3 : Train Data
# ---------------------------------------------------------

print("\nStep 3 : Train Data")

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data :", X_test.shape)

# Create Linear Regression object
model = LinearRegression()

# Train model
model.fit(X_train, Y_train)

print("\nModel training completed.")

# ---------------------------------------------------------
# Step 4 : Test Data
# ---------------------------------------------------------

print("\nStep 4 : Test Data")

Y_pred = model.predict(X_test)

print("Prediction completed.")

# ---------------------------------------------------------
# Step 5 : Display Predicted and Expected Values
# ---------------------------------------------------------

print("\nStep 5 : Predicted Values vs Expected Values")

result = pd.DataFrame({
    "Expected Sales": Y_test.values,
    "Predicted Sales": Y_pred
})

print(result)

# ---------------------------------------------------------
# Model Information
# ---------------------------------------------------------

print("\nModel Coefficients:")
print(model.coef_)

print("\nModel Intercept:")
print(model.intercept_)

print("\nModel Score:")
print(model.score(X_test, Y_test))