import pandas as pd

marks = pd.Series(
    [75, 55, 82, 60, 90],
    index=["Maths", "Python", "DBMS", "English", "DS"]
)

print(marks > 60)