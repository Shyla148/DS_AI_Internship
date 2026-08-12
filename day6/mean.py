import numpy as np
marks=np.array([[60,70,80],[70,80,90],[70,80,60]])
print("Marks of students in 3 subjects:\n",marks)
print("Mean of all elements:",np.mean(marks))
print("shape of marks array:",marks.shape)
print("\n")

r=np.mean(marks,axis=0)#row wise mean each subject
print("Mean of each subject:",r)
print("Shape of r array:",r.shape)
print("\n")
result=np.mean(marks,axis=1)#column wise mean each student
print("Mean of each student:",result)
print("Shape of result array:",result.shape)