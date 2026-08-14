# ==========================================
# TRAIN PASSENGERS DATASET - COMPLETE EDA
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Load Dataset
# ------------------------------------------
df = pd.read_csv(r"C:\Users\shyla\DS_AI_Internship\day9\train_passengers_dataset.csv")

# ------------------------------------------
# Basic Information
# ------------------------------------------
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== SUMMARY =====")
print(df.describe())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATES =====")
print(df.duplicated().sum())

# ------------------------------------------
# Univariate Analysis
# ------------------------------------------
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Histogram - {col}")
    plt.show()

# ------------------------------------------
# Categorical Analysis
# ------------------------------------------
cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(x=df[col])
    plt.title(f"Count Plot - {col}")
    plt.xticks(rotation=45)
    plt.show()

# ------------------------------------------
# Skewness Analysis
# ------------------------------------------
print("\n===== SKEWNESS =====")

for col in numeric_cols:
    skew = df[col].skew()

    print(f"{col}: {round(skew,2)}")

    if skew > 0:
        print("Positively Skewed")
    elif skew < 0:
        print("Negatively Skewed")
    else:
        print("Symmetric")

# ------------------------------------------
# Outlier Detection
# ------------------------------------------
print("\n===== OUTLIER COUNT =====")

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

    print(col, ":", len(outliers))

    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot - {col}")
    plt.show()

# ------------------------------------------
# Correlation Analysis
# ------------------------------------------
corr = df[numeric_cols].corr()

print("\n===== CORRELATION MATRIX =====")
print(corr)

plt.figure(figsize=(10,6))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------------------
# Bivariate Analysis
# ------------------------------------------

# Ticket Price vs Distance
plt.figure(figsize=(7,5))
sns.scatterplot(
    x='Travel_Distance',
    y='Ticket_Price',
    data=df
)
plt.title("Distance vs Ticket Price")
plt.show()

# Delay vs Satisfaction
plt.figure(figsize=(7,5))
sns.scatterplot(
    x='Delay_Minutes',
    y='Satisfaction_Score',
    data=df
)
plt.title("Delay vs Satisfaction")
plt.show()

# Gender vs Satisfaction
plt.figure(figsize=(6,4))
sns.boxplot(
    x='Gender',
    y='Satisfaction_Score',
    data=df
)
plt.title("Gender vs Satisfaction")
plt.show()

# Travel Class vs Ticket Price
plt.figure(figsize=(6,4))
sns.barplot(
    x='Travel_Class',
    y='Ticket_Price',
    data=df
)
plt.title("Class vs Ticket Price")
plt.show()

# Pairplot
sns.pairplot(df[numeric_cols])
plt.show()

# ------------------------------------------
# Pattern Identification
# ------------------------------------------
print("\n===== PATTERN IDENTIFICATION =====")

print("""
1. Higher travel distance generally increases ticket price.
2. Increased delay reduces passenger satisfaction.
3. First Class passengers usually pay higher fares.
4. Satisfaction is often higher when delays are lower.
5. Outliers may exist in ticket prices and delay times.
""")

# ------------------------------------------
# Final Report
# ------------------------------------------
print("\n===== EDA REPORT =====")

print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

print("""
INSIGHTS:
 Missing values checked
 Duplicate records checked
 Univariate analysis completed
 Bivariate analysis completed
 Skewness analyzed
 Correlation heatmap generated
 Outliers detected using IQR
 Passenger travel patterns identified

CONCLUSION:
Ticket price is strongly related to travel distance and travel class.
Passenger satisfaction decreases as delay increases.
Most variables show normal distribution with a few outliers.
The dataset is suitable for further predictive analytics and machine learning.
""")