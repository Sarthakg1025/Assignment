import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ==========================================================
# Step 1 : Get Data
# ==========================================================

def GetData():

    print("Step 1 : Getting Data")

    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    print(df)

    return df


# ==========================================================
# Step 2 : Clean, Prepare and Manipulate Data
# ==========================================================

def PrepareData(df):

    print("\nStep 2 : Preparing Data")

    # Remove unnecessary index column if it exists
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)

    # Create LabelEncoder objects
    weather_encoder = LabelEncoder()
    temperature_encoder = LabelEncoder()
    play_encoder = LabelEncoder()

    # Encode Weather
    df["Wether"] = weather_encoder.fit_transform(df["Wether"])

    # Encode Temperature
    df["Temperature"] = temperature_encoder.fit_transform(
        df["Temperature"]
    )

    # Encode Play
    df["Play"] = play_encoder.fit_transform(
        df["Play"]
    )

    print("\nEncoded Data:")
    print(df)

    return df, weather_encoder, temperature_encoder, play_encoder


# ==========================================================
# Step 3 : Train Data
# ==========================================================

def TrainData(X, Y):

    print("\nStep 3 : Training Data")

    # Create KNN classifier
    model = KNeighborsClassifier(n_neighbors=3)

    # Train model using complete dataset
    model.fit(X, Y)

    print("Training completed successfully.")

    return model


# ==========================================================
# Step 4 : Test Data
# ==========================================================

def TestData(
    model,
    weather_encoder,
    temperature_encoder,
    play_encoder
):

    print("\nStep 4 : Test Data")

    print("\nAvailable Weather:")
    print("1. Sunny")
    print("2. Overcast")
    print("3. Rainy")

    weather = input("\nEnter Weather: ")

    print("\nAvailable Temperature:")
    print("1. Hot")
    print("2. Mild")
    print("3. Cool")

    temperature = input("\nEnter Temperature: ")

    # Remove unnecessary spaces
    weather = weather.strip()
    temperature = temperature.strip()

    # Check whether Weather is valid
    if weather not in weather_encoder.classes_:

        print("\nInvalid Weather!")

        print(
            "Please enter one of:",
            list(weather_encoder.classes_)
        )

        return

    # Check whether Temperature is valid
    if temperature not in temperature_encoder.classes_:

        print("\nInvalid Temperature!")

        print(
            "Please enter one of:",
            list(temperature_encoder.classes_)
        )

        return

    # Convert Weather into numerical value
    weather_value = weather_encoder.transform(
        [weather]
    )[0]

    # Convert Temperature into numerical value
    temperature_value = temperature_encoder.transform(
        [temperature]
    )[0]

    # Create test data
    test_data = [
        [weather_value, temperature_value]
    ]

    # Predict
    prediction = model.predict(test_data)

    # Convert numerical prediction back to Yes / No
    result = play_encoder.inverse_transform(prediction)

    print("\n--------------------------------")
    print("Prediction :", result[0])
    print("--------------------------------")


# ==========================================================
# Step 5 : Calculate Accuracy
# ==========================================================

def CheckAccuracy(X, Y):

    print("\nStep 5 : Calculate Accuracy")

    # Divide dataset into training and testing data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("\nTraining records :", len(X_train))
    print("Testing records  :", len(X_test))

    # Create KNN model
    model = KNeighborsClassifier(n_neighbors=3)

    # Train model
    model.fit(X_train, Y_train)

    # Predict testing data
    Y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    print("\nActual values    :", list(Y_test))
    print("Predicted values :", list(Y_pred))

    print("\nAccuracy :", accuracy * 100, "%")


# ==========================================================
# Main Function
# ==========================================================

def main():

    # ------------------------------------------------------
    # Step 1 : Get Data
    # ------------------------------------------------------

    df = GetData()

    # ------------------------------------------------------
    # Step 2 : Prepare Data
    # ------------------------------------------------------

    (
        df,
        weather_encoder,
        temperature_encoder,
        play_encoder
    ) = PrepareData(df)

    # ------------------------------------------------------
    # Create Features and Target
    # ------------------------------------------------------

    # Features
    X = df[
        [
            "Wether",
            "Temperature"
        ]
    ]

    # Target
    Y = df["Play"]

    # ------------------------------------------------------
    # Step 3 : Train Data
    # ------------------------------------------------------

    model = TrainData(X, Y)

    # ------------------------------------------------------
    # Step 4 : Test Data
    # ------------------------------------------------------

    TestData(
        model,
        weather_encoder,
        temperature_encoder,
        play_encoder
    )

    # ------------------------------------------------------
    # Step 5 : Calculate Accuracy
    # ------------------------------------------------------

    CheckAccuracy(X, Y)


# ==========================================================
# Program Starting Point
# ==========================================================

if __name__ == "__main__":
    main()