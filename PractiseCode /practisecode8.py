from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt  

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,8,2,5,6,3,7,2]
z = [1,2,6,3,2,7,3,3,7,2]

x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-7,-8,-2,-5,-6,-3,-7,-2]
z2 = [-1,-2,-6,-3,-2,-7,-3,-3,-7,-2]

ax1.scatter(x, y, z)
ax1.scatter(x2, y2, z2)


plt.show()