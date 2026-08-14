import pandas as pd 
df= pd.read_csv('C:\\Users\\shyla\\DS_AI_Internship\\day7\\student_performance_dataset.csv')
print(df)

print("shape:",df.shape)
print("datatype:",df.dtypes)
print("missing values count:",df.isnull().sum())
print("duplicate row count:",df.duplicated().sum())
print("describe:",df.describe())
#remove duplicate rows
df = df.drop_duplicates().reset_index(drop=True)

df['Name'] = df["Name"].astype(str).str.strip().str.title()

df['Maths'] = df["Maths"].fillna(df["Maths"].mean())
df['Science'] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())
df[['Maths', 'Science', 'English']] = df[['Maths', 'Science', 'English']].astype(int)
df['Name'] = df['Name'].replace('Nan', 'Unknown')

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:")
print(df.shape)

print("\nCleaned Dataset:")
print(df)