import  pandas as pd
data=pd.Series([10,None,30,None])
print(data)
print(data.isnull())
print(data.fillna(0))