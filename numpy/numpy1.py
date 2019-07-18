import numpy as np
from matplotlib import pyplot as plt
a = np.array([1, 2, 3, 4], dtype='complex64')
# print(a)
# two rows and three columns
a = np.array([[1, 2, 3], [2, 3, 4], [4, 5, 6], [6, 7, 8]])
# print(a.shape)
# a.shape = (3, 4)  # change the rows form 2 to 3 by using (3,2) tuple
# print(a)
#print (a.ndim)

#a = np.arange(30)
#a = a.reshape(2,5,3)
# print(a)

#a = np.empty([2,3], dtype=float)
# print(a)

# a = np.ones((2, 300, 3), dtype=int)
# print(a)

x = np.arange(1,110) 
y = 2 * (x * x) + 5 
z = 2*x + 5*y + 10
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y, 'ob') 
plt.show()
