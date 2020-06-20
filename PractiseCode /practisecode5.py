import matplotlib.pyplot as plt 

days = [1,2,3,4,5]

Eating = [1,2,6,7]
Working = [4,5,6,2]
Playing = [4,5,3,2]
Sleeping = [6,5,6,2]

slices = [7,2,3,4]
activities = ['Eating', 'Working', 'Playing', 'Sleeping']
colors = ['c', 'r', 'k', 'm']

plt.pie(slices, colors=colors)
plt.show()