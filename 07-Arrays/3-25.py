import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# create y values
for n in x:
   y = y + [(math.pow(n,2))-3]

# print chart
plt.plot(x,y)
plt.show()
...