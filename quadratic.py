import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,6,7,8,9,]
y=[5,6,7,8,9,3,2,1,0]
plt.xlabel('x')
plt.ylabel('y=x^3+x^2+x+2')
plt.title('quardratic graph' )
plt.scatter(x,y)
plt.plot(x,y)
plt.show()