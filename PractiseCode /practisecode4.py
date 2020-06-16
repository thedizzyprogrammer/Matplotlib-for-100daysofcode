import matplotlib.pyplot as plt 

x = [1,2]

y = [5,7]

x2 = [1,2,3]

y2 = [20,21,29]


plt.scatter(x, y, label='First set of data')

plt.scatter(x2,y2, label='Second set of data')

plt.xlabel ('Var1')

plt.ylabel ('Var2')

plt.title('Example Graph\nPart of #100daysofcode')

plt.legend()

plt.show()