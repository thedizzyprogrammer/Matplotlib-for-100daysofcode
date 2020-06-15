#devoloped by thedizzyprogrammer

import matplotlib.pyplot as plt 

x = [1,2,3,4,5,6,7,8,9,10]

y = [1,2,3,4,5,6,7,8,9,10]

x2 = [1,2,3]

y2 = [20,21,29]


plt.bar(x2,y2, label='Bar Chart Example Number 2', color='grey')

plt.bar(x, y, label='Bar Chart Example Number 1')

plt.xlabel ('Var1')

plt.ylabel ('Var2')

plt.title('Example Graph\nPart of #100daysofcode')

plt.legend()

plt.show()