import numpy as np 
import pandas as pd
marks=[80,90,75]
x=pd.Series(marks,index=['Maths','Physics','Hindi'])
print(x)
print(x.index.to_list())