# ==========================================================
# BLOOD DONATION PREDICTION SYSTEM
# Real-World ML Problem
# ==========================================================

# Problem:
# Predict whether a registered donor is likely to donate blood
# in the next 3 months.

# Supervised Learning  : Classification
# Unsupervised Learning: Clustering
# ==========================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report

# ==========================================================
# STEP 1: LOAD DATASET
# ==========================================================

df = pd.read_csv("C:\\Users\\shyla\\DS_AI_Internship\\day11\\Blood_Donation_Prediction_Dataset (1).csv")

print("Dataset Preview")
print(df.head())

print("\nShape:", df.shape)

# ==========================================================
# STEP 2: DATA PREPROCESSING
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
# CLASSIFICATION
# ==========================================================

print("\n==============================")
print("SUPERVISED LEARNING")
print("==============================")

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

print("\nClassification Accuracy:")
print(round(accuracy_score(y_test, predictions), 2))

print("\nClassification Report")
print(classification_report(y_test, predictions))

# ==========================================================
# JUSTIFICATION:
# Classification is used because target output is:
# YES or NO
# ==========================================================

print("\nProblem Type: CLASSIFICATION")
print("Target Variable = Will_Donate_Next_3_Months")
print("Possible Outputs = Yes / No")

# ==========================================================
# STEP 4: UNSUPERVISED LEARNING
# CLUSTERING DONORS
# ==========================================================

print("\n==============================")
print("UNSUPERVISED LEARNING")
print("==============================")

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

print("\nCluster Assignment")
print(df[['Donor_ID', 'Cluster']].head(10))

print("\nCluster Count")
print(df['Cluster'].value_counts())

# ==========================================================
# SCENARIO:
#
# Cluster 0 -> Regular Donors
# Cluster 1 -> Occasional Donors
# Cluster 2 -> Inactive Donors
#
# This helps the blood bank send targeted campaigns.
# ==========================================================

# ==========================================================
# STEP 5: REGRESSION VS CLASSIFICATION
# ==========================================================

print("\n==============================")
print("REGRESSION VS CLASSIFICATION")
print("==============================")

print("""
Current Problem:
Predict whether donor will donate blood
in next 3 months.

Output:
YES or NO

Therefore:
CLASSIFICATION

If target were:

Days Until Next Donation

Example:
15 days
30 days
90 days

Then:
REGRESSION
because output is numerical.
""")

# ==========================================================
# STEP 6: DATA LEAKAGE
# ==========================================================

print("\n==============================")
print("DATA LEAKAGE")
print("==============================")

print("""
Example Leakage Feature:

Future_Donation_Date

or

Total_Donations_After_Prediction_Date

These contain future information.

The model would learn information
that would not be available during
real prediction.

Result:
Artificially high accuracy.
Poor real-world performance.
""")

# ==========================================================
# STEP 7: OVERFITTING
# ==========================================================

print("\n==============================")
print("OVERFITTING")
print("==============================")

overfit_model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

overfit_model.fit(X_train, y_train)

train_pred = overfit_model.predict(X_train)
test_pred = overfit_model.predict(X_test)

print("Training Accuracy:",
      accuracy_score(y_train, train_pred))

print("Testing Accuracy:",
      accuracy_score(y_test, test_pred))

print("""
Overfitting:
Model memorizes training data.

Effect:
Very high training accuracy
Lower testing accuracy

Poor performance on new donors.
""")

# ==========================================================
# STEP 8: UNDERFITTING
# ==========================================================

print("\n==============================")
print("UNDERFITTING")
print("==============================")

underfit_model = DecisionTreeClassifier(
    max_depth=1,
    random_state=42
)

underfit_model.fit(X_train, y_train)

train_pred2 = underfit_model.predict(X_train)
test_pred2 = underfit_model.predict(X_test)

print("Training Accuracy:",
      accuracy_score(y_train, train_pred2))

print("Testing Accuracy:",
      accuracy_score(y_test, test_pred2))

print("""
Underfitting:
Model is too simple.

Effect:
Low training accuracy
Low testing accuracy

Fails to learn donation patterns.
""")

# ==========================================================
# FINAL CONCLUSION
# ==========================================================

print("\n==============================")
print("CONCLUSION")
print("==============================")

print("""
Supervised Learning:
Used Classification to predict
whether a donor will donate blood.

Unsupervised Learning:
Used K-Means Clustering to group donors.

Classification:
Preferred because output is Yes/No.

Data Leakage:
Future donation information must not be used.

Overfitting:
Model memorizes training data.

Underfitting:
Model is too simple to learn patterns.
""")
graph_df = df.copy()
print("\nShape:", df.shape)
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# GRAPH 1: DONATION RATE
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
# GRAPH 2: BLOOD GROUP DISTRIBUTION
# ==========================================================

plt.figure(figsize=(8,5))

sns.countplot(
    x='Blood_Group',
    data=df
)

plt.title("Blood Group Distribution")
plt.xlabel("Blood Group")
plt.ylabel("Count")

plt.show()


# ==========================================================
# GRAPH 3: AGE VS PREVIOUS DONATIONS
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
# GRAPH 4: DONOR CLUSTERS
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
# GRAPH 5: DONATION RATE PIE CHART
# ==========================================================

donation_counts = df['Will_Donate_Next_3_Months'].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    donation_counts,
    labels=['No','Yes'],
    autopct='%1.1f%%'
)

plt.title("Donation Prediction Percentage")

plt.show()