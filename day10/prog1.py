import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\shyla\DS_AI_Internship\day10\first_15_records.csv")
# Target column = last column
target_col = df.columns[-1]
target = df[target_col]

print("Dataset Shape:", df.shape)
print("Target Column:", target_col)
print("Data Type:", target.dtype)
print("Unique Values:", target.nunique())

# Check problem type
if target.dtype == "object" or target.nunique() <= 10:
    print("\nMachine Learning Type : Supervised Learning")
    print("Problem Type          : Classification")

    print("\nInsights:")
    print("- Target contains categories/classes.")
    print("- Model predicts a class label.")
    print("- Examples: Pass/Fail, Yes/No, Survived/Not Survived.")

else:
    print("\nMachine Learning Type : Supervised Learning")
    print("Problem Type          : Regression")

    print("\nInsights:")
    print("- Target contains continuous numerical values.")
    print("- Model predicts a number.")
    print("- Examples: Price, Salary, Marks, Temperature.")
    
    