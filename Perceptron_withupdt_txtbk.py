import random
from tkinter import END
import numpy as np

learning_rate=2

  
x=np.array([[0.25,0.353],[0.25,0.471],[0.5,0.353],[0.5,0.647],[0.75,0.705],[0.75,0.882],[1,0.705],[1,1],[1,1],[0.25,0.471]],dtype=np.float32)   # input array
weight=np.array([[0,0],[0,0]],dtype=np.float32)          # weight matrix
y=np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],dtype=np.float32)     # obtained output
y_desired=np.array([[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[1,0],[1,0]],dtype=np.float32)    # Desired output array
bias=0                                  # Bias value
weight_length=len(weight)
print(weight_length)
for i in range(len(weight)):
   for j in range(len(weight)):
       weight[i,j] =np.random.uniform() #Assigned some random weights in [0,1] range
       print(weight[i,j])  

for k in range(len(x)):
   for i in range (len(weight)):
      for j in range(len(weight)):
         y[k,i]=y[k,i]+x[k,j]*weight[i,j]
      if y[k,i]>0.5:
         y[k,i]=1
      else:
         y[k,i]=0

         # weight update code
   for i_1 in range(len(weight)):
      if y[k,i_1]!= y_desired[k,i_1]:
          error=y_desired[k,i_1]-y[k,i_1]
          for j_1 in range(len(weight)):
            weight[i_1,j_1]=weight[i_1,j_1]+learning_rate*error*x[k,i_1]
            
         
print(x)
print(weight)
print(y)

