import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,6,7,8,9,]
y=[5,8,10,14,15,18,25,29,30]
plt.xlabel("x")
plt.ylabel("y=x^3+x^2+x+2")
plt.title("quardratic graph" )
plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,5,10,15,20,25,30,35,40,50])
plt.plot(x,y ,label="**x")
plt.show()