import matplotlib.pyplot as plt 

x = [1,2,3]

y = [5,7,20]

x2 = [1,2,3]

y2 = [20,21,29]


plt.plot(x, y, label='First Line')

plt.plot(x2,y2, label='Second Line')

plt.xlabel ('Var1')

plt.ylabel ('Var2')

plt.title('Example Graph\nPart of #100daysofcode')

plt.legend()

plt.show()