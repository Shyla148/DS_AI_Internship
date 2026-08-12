import numpy as np
marks=np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])
print("Marks of students in 3 subjects:\n",marks)
print("Median of all elements:",np.median(marks))
print("shape of marks array:",marks.shape)
print("\n")

r=np.median(marks,axis=0)#row wise median each subject
print("Median of each subject:",r)
print("Shape of r array:",r.shape)
print("\n")

result=np.median(marks,axis=1)#column wise median each student
print("Median of each student:",result)
print("Shape of result array:",result.shape)