from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
 
np.random.seed(10)
N=300
x=np.random.rand(N)*2-1
y=np.random.rand(N)*2-1
 
z=x*x+y*y
 
fig1 = plt.figure()
ax = Axes3D(fig1)
ax.scatter3D(x,y,z,c='r', marker='s')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.legend(loc='upper left')
plt.show()
