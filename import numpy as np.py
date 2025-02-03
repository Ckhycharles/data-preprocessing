
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=[1,2,3,4]#stating the x axis value as an array
y=[0,2,4,6]# stating the y axis values as an array
x2=np.arange(0,5,0.5)#making an array of avlues ranging from 0 to five with a class difference of 0.5
print(x2)#printing the arrray
plt.figure(figsize=(4,4),dpi=300)

plt.plot(x2[:7],x2[:7]**2,'r',label='x2**2')#plot function showing the attrbutes of the line graph
#:7tellss the compiler to print values ranging between 0 and seven 
#'r' assigns a red color to the line drawn 
#label show what will be displayed on top of the graph
plt.plot(x2[6:],x2[6:]**2,'r^--',label='x2**2')#
plt.plot(x,y ,'b^-.',label='2x',color='brown',marker='*')
#inputing a scale to a graph
plt.xticks([1,2,3,4,5])
#shows the key to be used for the x axis
plt.yticks([0,2,4,6,8,10])
#axes=plt.subplots(nrows=4,ncols=1)

#shos the key to be used for the y axis 
#to lable the axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('linear graph')
plt.legend()


#to visualize the graph
plt.show()