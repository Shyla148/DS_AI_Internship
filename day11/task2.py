# ==========================================================
# BLOOD DONATION PREDICTION SYSTEM
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ==========================================================
# STEP 1: LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\shyla\DS_AI_Internship\day11\Blood_Donation_Prediction_Dataset (1).csv"
)

print("Dataset Preview")
print(df.head())

print("\nDataset Shape:", df.shape)

# ==========================================================
# STEP 2: LABEL ENCODING
# ==========================================================

encoder = LabelEncoder()

df['Gender'] = encoder.fit_transform(df['Gender'])
df['Blood_Group'] = encoder.fit_transform(df['Blood_Group'])
df['Health_Status'] = encoder.fit_transform(df['Health_Status'])
df['Will_Donate_Next_3_Months'] = encoder.fit_transform(
    df['Will_Donate_Next_3_Months']
)

# ==========================================================
# STEP 3: SUPERVISED LEARNING
# ==========================================================

print("\n===== SUPERVISED LEARNING =====")

X = df.drop(
    ['Donor_ID', 'Will_Donate_Next_3_Months'],
    axis=1
)

y = df['Will_Donate_Next_3_Months']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

# ==========================================================
# EVALUATION METRICS
# ==========================================================

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

cm = confusion_matrix(y_test, predictions)

print("\n===== MODEL EVALUATION =====")

print("Accuracy :", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall   :", round(recall, 2))
print("F1 Score :", round(f1, 2))

print("\nConfusion Matrix")
print(cm)

print("\nClassification Report")
print(classification_report(y_test, predictions))

# ==========================================================
# STEP 4: UNSUPERVISED LEARNING
# ==========================================================

print("\n===== K-MEANS CLUSTERING =====")

cluster_data = df.drop(
    ['Donor_ID', 'Will_Donate_Next_3_Months'],
    axis=1
)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(cluster_data)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df['Cluster'] = kmeans.fit_predict(scaled_data)

print(df[['Donor_ID', 'Cluster']].head())

print("\nCluster Count")
print(df['Cluster'].value_counts())

# ==========================================================
# GRAPH 1
# DONATION RATE
# ==========================================================

plt.figure(figsize=(6,4))

sns.countplot(
    x='Will_Donate_Next_3_Months',
    data=df
)

plt.title("Donation Prediction Rate")
plt.xlabel("Will Donate Next 3 Months")
plt.ylabel("Number of Donors")
plt.show()

# ==========================================================
# GRAPH 2
# BLOOD GROUP DISTRIBUTION
# ==========================================================

plt.figure(figsize=(7,4))

sns.countplot(
    x='Blood_Group',
    data=df
)

plt.title("Blood Group Distribution")
plt.xlabel("Blood Group")
plt.ylabel("Count")
plt.show()

# ==========================================================
# GRAPH 3
# AGE VS PREVIOUS DONATIONS
# ==========================================================

plt.figure(figsize=(7,5))

plt.scatter(
    df['Age'],
    df['Previous_Donations']
)

plt.title("Age vs Previous Donations")
plt.xlabel("Age")
plt.ylabel("Previous Donations")
plt.show()

# ==========================================================
# GRAPH 4
# DONOR CLUSTERS
# ==========================================================

plt.figure(figsize=(7,5))

plt.scatter(
    df['Age'],
    df['Previous_Donations'],
    c=df['Cluster']
)

plt.title("Donor Clusters")
plt.xlabel("Age")
plt.ylabel("Previous Donations")
plt.show()

# ==========================================================
# GRAPH 5
# PIE CHART
# ==========================================================

donation_counts = df[
    'Will_Donate_Next_3_Months'
].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    donation_counts,
    labels=['No', 'Yes'],
    autopct='%1.1f%%'
)

plt.title("Donation Prediction Percentage")
plt.show()

# ==========================================================
# CONCLUSION
# ==========================================================

print("\n===== CONCLUSION =====")

print("""
1. Supervised Learning:
   Logistic Regression used for classification.

2. Unsupervised Learning:
   K-Means used for donor segmentation.

3. Classification:
   Output is Yes/No.

4. Data Leakage:
   Future donation information should not be used.

5. Overfitting:
   Model memorizes training data.

6. Underfitting:
   Model is too simple and misses patterns.
""")