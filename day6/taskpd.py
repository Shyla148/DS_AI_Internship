import pandas as pd

marks=pd.Series([85,90,78],index=['Maths','Physics','chemistry'])
print("marks:",marks)

 #accessing the elements of series using positional index
print("first marks:",marks.iloc[0])
#acessing the elements of series using index label 
print("second marks:",marks['Physics'])
print("third marks:",marks['chemistry'])

print("\nvalues")
print(marks.values)

print("\nindex")
print(marks.index)
#boolean masking -marks above 60
print("\nmarks above 85")
passed=marks[marks>85]
print(passed)