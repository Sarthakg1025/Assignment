import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = 19 * "-"

# Load dataset for subsequent operations
df = pd.read_csv('student_performance_ml.csv')
X = df[
    [
        'StudyHours',
        'Attendance',
        'PreviousScore',
        'AssignmentsCompleted',
        'SleepHours',
    ]
]
y = df['FinalResult']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================
# Question 1: Train DecisionTreeClassifier
# ==========================================
print(Border)
print("--- Question 1 ---")
print(Border)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("DecisionTreeClassifier model successfully created and trained.")


# ==========================================
# Question 2: Predict and Display Results
# ==========================================
print("\n" + Border)
print("--- Question 2 ---")
print(Border)

y_pred = model.predict(X_test)

results_df = pd.DataFrame(
    {'Actual': y_test.values, 'Predicted': y_pred}, index=X_test.index
)
print("Predicted values along with actual values:")
print(results_df)


# ==========================================
# Question 3: Model Accuracy
# ==========================================
print("\n" + Border)
print("--- Question 3 ---")
print(Border)

acc = accuracy_score(y_test, y_pred) * 100
print(f"Model Accuracy: {acc:.2f}%")


# ==========================================
# Question 4: Confusion Matrix & Concepts
# ==========================================
print("\n" + Border)
print("--- Question 4 ---")
print(Border)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=['Fail (0)', 'Pass (1)']
)

print("Displaying Confusion Matrix...")
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

print("\nConcept Explanations:")
print(
    "• True Positive (TP): Students who actually Passed (1) and were correctly predicted as Passed (1)."
)
print(
    "• True Negative (TN): Students who actually Failed (0) and were correctly predicted as Failed (0)."
)
print(
    "• False Positive (FP): Students who actually Failed (0) but were incorrectly predicted as Passed (1)."
)
print(
    "• False Negative (FN): Students who actually Passed (1) but were incorrectly predicted as Failed (0)."
)


# ==========================================
# Question 5: Training vs Testing Accuracy
# ==========================================
print("\n" + Border)
print("--- Question 5 ---")
print(Border)

train_acc = accuracy_score(y_train, model.predict(X_train)) * 100
test_acc = accuracy_score(y_test, y_pred) * 100

print(f"Training Accuracy: {train_acc:.2f}%")
print(f"Testing Accuracy: {test_acc:.2f}%")

print("\nObservation:")
print(
    "Both training and testing accuracies are 100%. The model generalizes perfectly to the test set without overfitting (high train, low test accuracy) or underfitting (low train, low test accuracy)."
)


# ==========================================
# Question 6: Decision Trees with Various Max Depths
# ==========================================
print("\n" + Border)
print("--- Question 6 ---")
print(Border)

depths = [1, 3, None]
for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    d_acc = accuracy_score(y_test, dt.predict(X_test)) * 100
    print(f"Testing Accuracy for max_depth={depth}: {d_acc:.2f}%")

print("\nObservations:")
print(
    "Even with a max_depth of 1, the Decision Tree achieves 100% testing accuracy. This indicates that the dataset is easily separable using a single feature threshold split."
)


# ==========================================
# Question 7: Predict Outcome for a New Student
# ==========================================
print("\n" + Border)
print("--- Question 7 ---")
print(Border)

new_student = pd.DataFrame(
    [[6, 85, 66, 7, 7]],
    columns=[
        'StudyHours',
        'Attendance',
        'PreviousScore',
        'AssignmentsCompleted',
        'SleepHours',
    ],
)

prediction = model.predict(new_student)[0]
result_label = "Pass" if prediction == 1 else "Fail"

print(f"Prediction result for the student: {prediction} ({result_label})")
print(f"Will the student Pass or Fail? The student will {result_label}.")


# ==========================================
# Question 8: Single Structured Python Program
# ==========================================
print("\n" + Border)
print("--- Question 8 ---")
print(Border)
print(
    "A complete, structured end-to-end program execution combining steps 1 through 7:"
)

# 1. Dataset loading
df_full = pd.read_csv('student_performance_ml.csv')

# 2. Data analysis
print("\n[Step 1 & 2] Class Distribution:\n", df_full['FinalResult'].value_counts())

# 3. Visualization
plt.figure(figsize=(6, 4))

'''sns.countplot(data=df_full, x='FinalResult', palette='Set2')'''
plt.title('Pass vs Fail Distribution')
plt.xlabel('Final Result (0=Fail, 1=Pass)')
plt.ylabel('Count')
plt.show()

# 4. Train-test split
X_full = df_full[
    [
        'StudyHours',
        'Attendance',
        'PreviousScore',
        'AssignmentsCompleted',
        'SleepHours',
    ]
]
y_full = df_full['FinalResult']
X_tr, X_te, y_tr, y_te = train_test_split(
    X_full, y_full, test_size=0.2, random_state=42
)

# 5. Model training
final_model = DecisionTreeClassifier(random_state=42)
final_model.fit(X_tr, y_tr)

# 6. Prediction
y_te_pred = final_model.predict(X_te)

# 7. Accuracy calculation
final_acc = accuracy_score(y_te, y_te_pred) * 100
print(f"\n[Step 7] Final Test Accuracy: {final_acc:.2f}%")

# 8. Confusion matrix generation
cm_final = confusion_matrix(y_te, y_te_pred)
disp_final = ConfusionMatrixDisplay(
    confusion_matrix=cm_final, display_labels=['Fail', 'Pass']
)
disp_final.plot()
plt.title('Final Model Confusion Matrix')
plt.show()

# 9. Final conclusion
print(
    "\n[Step 9] Final Conclusion: The Decision Tree Classifier successfully predicts student performance with 100% accuracy on the test data."
)