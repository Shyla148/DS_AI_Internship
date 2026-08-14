# ==========================================
# COMPLETE EDA PROJECT
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------
df = pd.read_csv(r"C:\Users\shyla\DS_AI_Internship\day9\student_performance_dataset (1).csv")
print(df)
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

# ------------------------------------------
# 2. Basic Information
# ------------------------------------------
print("\n========== DATASET INFO ==========")
print(df.info())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# ------------------------------------------
# 3. Missing Values
# ------------------------------------------
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# ------------------------------------------
# 4. Duplicate Values
# ------------------------------------------
print("\n========== DUPLICATES ==========")
print(df.duplicated().sum())

# ------------------------------------------
# 5. Univariate Analysis
# ------------------------------------------
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Histogram of {col}")
    plt.show()

# ------------------------------------------
# 6. Box Plot (Outlier Detection)
# ------------------------------------------
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# ------------------------------------------
# 7. Skewness Analysis
# ------------------------------------------
print("\n========== SKEWNESS ==========")

for col in numeric_cols:
    skew_value = df[col].skew()
    print(f"{col}: {skew_value:.2f}")

    if skew_value > 0:
        print(" Positively Skewed")
    elif skew_value < 0:
        print(" Negatively Skewed")
    else:
        print(" Symmetrical")

# ------------------------------------------
# 8. Correlation Analysis
# ------------------------------------------
corr_matrix = df[numeric_cols].corr()

print("\n========== CORRELATION MATRIX ==========")
print(corr_matrix)

plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix,
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------------------
# 9. Bivariate Analysis
# ------------------------------------------
if len(numeric_cols) >= 2:

    plt.figure(figsize=(7,5))
    sns.scatterplot(
        x=df[numeric_cols[0]],
        y=df[numeric_cols[1]]
    )

    plt.title(
        f"{numeric_cols[0]} vs {numeric_cols[1]}"
    )

    plt.show()

# Pairplot
sns.pairplot(df[numeric_cols])
plt.show()

# ------------------------------------------
# 10. Outlier Detection using IQR
# ------------------------------------------
print("\n========== OUTLIER COUNT ==========")

for col in numeric_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df[col] < lower) |
        (df[col] > upper)
    ]

    print(f"{col}: {len(outliers)} outliers")

# ------------------------------------------
# 11. Pattern Identification
# ------------------------------------------
print("\n========== PATTERN IDENTIFICATION ==========")

for col in numeric_cols:

    mean = df[col].mean()
    median = df[col].median()

    print(f"\n{col}")
    print(f"Mean   : {mean:.2f}")
    print(f"Median : {median:.2f}")

    if mean > median:
        print("Right Skewed Distribution")
    elif mean < median:
        print("Left Skewed Distribution")
    else:
        print("Approximately Symmetric")

# ------------------------------------------
# 12. Final EDA Report
# ------------------------------------------
print("\n========== EDA REPORT ==========")

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nKey Findings:")
print("- Checked missing values")
print("- Checked duplicate records")
print("- Performed univariate analysis")
print("- Performed bivariate analysis")
print("- Calculated skewness")
print("- Generated correlation heatmap")
print("- Detected outliers using IQR")
print("- Identified distribution patterns")

print("\nEDA Completed Successfully!")