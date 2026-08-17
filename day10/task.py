# Household Electricity Consumption Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Sample Dataset
df = pd.read_csv(
    r"C:\Users\shyla\DS_AI_Internship\day10\household_electricity_dataset_100_rows.csv"
)
print(df.head())

# Features and Target
X = df[['Temperature', 'Appliances_Used',
        'Time_of_Day', 'Previous_Usage']]
y = df['Electricity_Consumption']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# New Prediction
new_data = pd.DataFrame({
    'Temperature': [30],
    'Appliances_Used': [7],
    'Time_of_Day': [14],
    'Previous_Usage': [18]
})

prediction = model.predict(new_data)

print("\nPredicted Electricity Consumption:",
      round(prediction[0], 2), "kWh")