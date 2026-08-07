import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

Border="-"*30

############################################
# Step 1 : Load the dataset
############################################
print(Border)
print("Step 1 : Load the data set")
print(Border)

DataPath="student_performance_ml.csv"

df=pd.read_csv(DataPath)

print("Dataset Loaded Successfully")
print("Initial entries from dataset are :")
print(df.head())

############################################
# Step 2 : Decide Independent & Dependent Variables
############################################
print(Border)
print("Step 2 : Decide Independent & Dependent Variables")
print(Border)

# X : Independent Variable / Features
# Y : Dependent Variable / Labels
features_cols= ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]

X=df[features_cols]
Y=df["FinalResult"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

############################################
# Step 3 : Split the dataset for training and testing
############################################
print(Border)
print("Step 3 : Split the dataset for training and testing")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Dataset splitting activity done..")
print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

############################################
# Step 4 : Build & Train Baseline Model
############################################
print(Border)
print("Step 4 : Build & Train Baseline Model")
print(Border)

model = DecisionTreeClassifier(random_state=42)
print("Model get created ..")

model.fit(X_train,Y_train)
print("Model trained ..")

Y_pred=model.predict(X_test)
base_accuracy = accuracy_score(Y_test,Y_pred)
print("Baseline Accuracy : ", base_accuracy * 100)

############################################
# Assignment Task 1 : Feature Importances
############################################
print(Border)
print("Assignment Task 1 : Feature Importances")
print(Border)

importances = model.feature_importances_
print("Feature Importances:")
for i, col in enumerate(features_cols):
    print(f"{col} : {importances[i]}")

print("Most contributing feature : ", features_cols[importances.argmax()])
print("Least contributing feature : ", features_cols[importances.argmin()])

############################################
# Assignment Task 2 : Remove SleepHours
############################################
print(Border)
print("Assignment Task 2 : Remove SleepHours")
print(Border)

X_no_sleep = X.drop("SleepHours", axis=1)
X_train_ns, X_test_ns, Y_train_ns, Y_test_ns = train_test_split(X_no_sleep, Y, test_size=0.2, random_state=42)

model_ns = DecisionTreeClassifier(random_state=42)
model_ns.fit(X_train_ns, Y_train_ns)
acc_ns = accuracy_score(Y_test_ns, model_ns.predict(X_test_ns))

print("Accuracy without SleepHours : ", acc_ns * 100)

############################################
# Assignment Task 3 : Train with StudyHours & Attendance
############################################
print(Border)
print("Assignment Task 3 : StudyHours & Attendance Only")
print(Border)

X_2f = X[['StudyHours', 'Attendance']]
X_train_2f, X_test_2f, Y_train_2f, Y_test_2f = train_test_split(X_2f, Y, test_size=0.2, random_state=42)

model_2f = DecisionTreeClassifier(random_state=42)
model_2f.fit(X_train_2f, Y_train_2f)
acc_2f = accuracy_score(Y_test_2f, model_2f.predict(X_test_2f))

print("Accuracy with only StudyHours & Attendance : ", acc_2f * 100)

############################################
# Assignment Task 4 : Predict for 5 New Students
############################################
print(Border)
print("Assignment Task 4 : Predict for 5 New Students")
print(Border)

new_data = pd.DataFrame({
    'StudyHours': [2, 8, 5, 1, 6],
    'Attendance': [50, 95, 75, 40, 85],
    'PreviousScore': [45, 90, 70, 35, 80],
    'AssignmentsCompleted': [2, 10, 6, 1, 8],
    'SleepHours': [8, 7, 6, 9, 7]
})

new_pred = model.predict(new_data)
new_data['Predicted_FinalResult'] = new_pred
print("Predictions for new students:\n", new_data)

############################################
# Assignment Task 5 : Manually Calculate Accuracy
############################################
print(Border)
print("Assignment Task 5 : Manually Calculate Accuracy")
print(Border)

manual_acc = (Y_test == Y_pred).sum() / len(Y_test)
print("Manual Accuracy : ", manual_acc * 100)
print("Matches sklearn accuracy? ", manual_acc == base_accuracy)

############################################
# Assignment Task 6 : Identify Misclassified
############################################
print(Border)
print("Assignment Task 6 : Identify Misclassified")
print(Border)

misclassified_mask = Y_test != Y_pred
misclassified_students = X_test[misclassified_mask].copy()
misclassified_students['Expected'] = Y_test[misclassified_mask]
misclassified_students['Predicted'] = Y_pred[misclassified_mask]

print("Number of misclassified students : ", len(misclassified_students))
print("Misclassified Rows :\n", misclassified_students)

############################################
# Assignment Task 7 : Train with Different Random States
############################################
print(Border)
print("Assignment Task 7 : Compare Random States")
print(Border)

for rs in [0, 10, 42]:
    X_train_rs, X_test_rs, Y_train_rs, Y_test_rs = train_test_split(X, Y, test_size=0.2, random_state=rs)
    model_rs = DecisionTreeClassifier(random_state=rs)
    model_rs.fit(X_train_rs, Y_train_rs)
    acc_rs = accuracy_score(Y_test_rs, model_rs.predict(X_test_rs))
    print(f"Accuracy with random_state = {rs} : {acc_rs * 100}%")

############################################
# Assignment Task 8 : Decision Tree Visualization
############################################
print(Border)
print("Assignment Task 8 : Decision Tree Visualization")
print(Border)

plt.figure(figsize=(10,6))
plot_tree(model, feature_names=features_cols, class_names=['Fail', 'Pass'], filled=True)
plt.title("Student Performance Decision Tree")
plt.savefig("tree_visualization.png")
print("Tree visual saved as 'tree_visualization.png'")

root_feature = features_cols[model.tree_.feature[0]]
print("Feature at the root node : ", root_feature)

############################################
# Assignment Task 9 : Create PerformanceIndex
############################################
print(Border)
print("Assignment Task 9 : Create PerformanceIndex")
print(Border)

df_pi = df.copy()
df_pi['PerformanceIndex'] = (df_pi['StudyHours'] * 2) + df_pi['Attendance']
X_pi = df_pi[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours', 'PerformanceIndex']]

X_train_pi, X_test_pi, Y_train_pi, Y_test_pi = train_test_split(X_pi, Y, test_size=0.2, random_state=42)
model_pi = DecisionTreeClassifier(random_state=42)
model_pi.fit(X_train_pi, Y_train_pi)
acc_pi = accuracy_score(Y_test_pi, model_pi.predict(X_test_pi))

print("Accuracy with PerformanceIndex : ", acc_pi * 100)

############################################
# Assignment Task 10 : Train model with max_depth = None
############################################
print(Border)
print("Assignment Task 10 : Overfitting Test")
print(Border)

model_overfit = DecisionTreeClassifier(max_depth=None, random_state=42)
model_overfit.fit(X_train, Y_train)

train_acc = accuracy_score(Y_train, model_overfit.predict(X_train))
test_acc = accuracy_score(Y_test, model_overfit.predict(X_test))

print("Training accuracy : ", train_acc * 100)
print("Testing accuracy : ", test_acc * 100)
print("Explanation: If training accuracy is 100% but testing is lower, the model is overfitting by memorizing the training data.")