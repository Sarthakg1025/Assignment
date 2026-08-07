import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border=19*"-"
# ==========================================
# Question 1: Load and Display Dataset Info
# ==========================================
print(Border)
print("--- Question 1 ---")
print(Border)
# Load dataset
df = pd.read_csv('student_performance_ml.csv')

print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())
print("\nTotal number of rows and columns:", df.shape)
print("\nList of column names:", df.columns.tolist())
print("\nData types of each column:\n", df.dtypes)


# ==========================================
# Question 2: Pass/Fail Counts
# ==========================================
print(Border)
print("--- Question 2 ---")
print(Border)
total_students = len(df)
passed = (df['FinalResult'] == 1).sum()
failed = (df['FinalResult'] == 0).sum()

print(f"Total students in the dataset: {total_students}")
print(f"Students Passed (1): {passed}")
print(f"Students Failed (0): {failed}")


# ==========================================
# Question 3: Pandas Functions (Averages, Max, Min)
# ==========================================
print("\n--- Question 3 ---")
print("Average StudyHours:", df['StudyHours'].mean())
print("Average Attendance:", df['Attendance'].mean())
print("Maximum PreviousScore:", df['PreviousScore'].max())
print("Minimum SleepHours:", df['SleepHours'].min())


# ==========================================
# Question 4: Distribution of FinalResult
# ==========================================
print("\n--- Question 4 ---")
counts = df['FinalResult'].value_counts()
percentages = df['FinalResult'].value_counts(normalize=True) * 100

print("Value counts for FinalResult:\n", counts)
print("\nPercentage of Pass/Fail students:\n", percentages)
print("\nJustification:")
print("The dataset is reasonably balanced. While passed students make up 60% of the data and failed students make up 40%, the ratio is mild enough for standard machine learning algorithms to process without severe class imbalance issues.")


# ==========================================
# Question 5: Dataset Value Analysis
# ==========================================
print("\n--- Question 5 ---")
print("Observations:")
print("1. Higher StudyHours drastically increase the chance of passing. All students who studied 4.5 hours or more passed.")
print("2. Higher Attendance directly improves the FinalResult. Students with attendance above 75% passed consistently.")
print("3. Both factors (StudyHours and Attendance) show strict thresholds where performance dictates success or failure.")


# ==========================================
# Question 6: Histogram of StudyHours
# ==========================================
print("\nGenerating Plot for Question 6...")
plt.figure(figsize=(8, 5))
plt.hist(df['StudyHours'], bins=8, color='skyblue', edgecolor='black')
plt.title('Histogram of StudyHours')
plt.xlabel('Study Hours')
plt.ylabel('Frequency')
plt.show()

print("Explanation: The distribution is bimodal/uniform, splitting students fairly evenly between a lower study-hour group (1-4 hours) and a higher study-hour group (5-8.5 hours).")


# ==========================================
# Question 7: Scatter plot (StudyHours vs PreviousScore)
# ==========================================
print("\nGenerating Plot for Question 7...")
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x='StudyHours', 
    y='PreviousScore', 
    hue='FinalResult', 
    palette={0: 'red', 1: 'green'},
    s=80
)
plt.title('StudyHours vs PreviousScore')
plt.xlabel('Study Hours')
plt.ylabel('Previous Score')
plt.legend(title='FinalResult (0=Fail, 1=Pass)')
plt.show()


# ==========================================
# Question 8: Boxplot for Attendance
# ==========================================
print("\nGenerating Plot for Question 8...")
plt.figure(figsize=(6, 5))
sns.boxplot(y=df['Attendance'], color='lightgreen')
plt.title('Boxplot for Attendance')
plt.ylabel('Attendance (%)')
plt.show()

# Outlier check using IQR
q1 = df['Attendance'].quantile(0.25)
q3 = df['Attendance'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['Attendance'] < lower_bound) | (df['Attendance'] > upper_bound)]
print(f"Number of Attendance outliers present: {len(outliers)}")


# ==========================================
# Question 9: AssignmentsCompleted vs FinalResult
# ==========================================
print("\nGenerating Plot for Question 9...")
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='AssignmentsCompleted', hue='FinalResult', palette={0: 'red', 1: 'green'})
plt.title('Assignments Completed vs Final Result')
plt.xlabel('Assignments Completed')
plt.ylabel('Student Count')
plt.show()

print("Observation: Completing 6 or more assignments guarantees passing in this dataset, while completing 4 or fewer results in a failure. 5 assignments is the tipping point.")


# ==========================================
# Question 10: SleepHours vs FinalResult
# ==========================================
print("\nGenerating Plot for Question 10...")
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='SleepHours', hue='FinalResult', palette={0: 'red', 1: 'green'})
plt.title('Sleep Hours vs Final Result')
plt.xlabel('Sleep Hours')
plt.ylabel('Student Count')
plt.show()

print("Explanation:")
print("No, sleeping more alone does not guarantee success. " 
        "While everyone getting 7-8 hours passed and those getting 5 hours failed, SleepHours is a confounding variable. " 
        "It correlates with healthy study routines, " 
        "but success ultimately requires the actual effort of studying and completing assignments.")