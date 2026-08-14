import matplotlib.pyplot as plt
x=[10,20,30,40,50,44,67,89,90,77]
y=[22,44,66,88,99,55,77,90,80,100]
plt.bar(x,y)
plt.show()


A=[1,2,3,4,5]
B=[5,4,3,2,1]
plt.bar(A,B,color='g',width=0.5)
plt.show()


categories = ['A', 'B', 'C', 'D', 'E']
values=[11,23,100,67,89]
plt.bar(categories,values,color='y',width=0.2)
plt.show()