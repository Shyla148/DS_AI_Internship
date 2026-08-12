import pandas as pd
import numpy as np
x={"math":80,"science":85,"english":80}
y=pd.Series(x)
print(y)

print("\n")
print("y greaterthan 80:")
print(y[y>80])
print("\n")

print("Index of the third element WITH values")
print(y.index[2],":",y.iloc[2])
print(y.index[2])