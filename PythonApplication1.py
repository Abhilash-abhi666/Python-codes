import random
import numpy as np
  
x=np.array([[0,1],[0,0],[1,0],[1,1]],dtype=np.float32)   # input array
#x=np.array([1,1],dtype=np.float32)
weight=np.array([[0,0],[0,0]],dtype=np.float32)    # weight matrix
y=np.array([[0,1],[0,0],[1,0],[1,1]],dtype=np.float32)    # output array
bias=0                                  # Bias value
net=bias                                # net value
k=0;
for i in range(len(x)-2):
   for j in range(len(weight[0])):
       weight[i,j] =round(random.uniform(0,1),2) #Assigned some random weights in [0,1] range
       
for k in range(len(x)-1):
   for i in range (len(weight[0])):
      for j in range(len(weight[0])):
          y[k,i]=y[k,i]+x[i,j]*weight[i,j]
      if y[k,i]>0.5:
        y[k,i]=1
      else:
        y[k,i]=0
print(x)
print(weight)
print(y)
