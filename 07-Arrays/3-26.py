import matplotlib.pyplot as plt
import math
x = []
y = []
#create  x values
for n in range(0,361):
    x = x + [n]

#create y values

for n in x:
    y = y + [math.sin(n/57.3)]

print(y)
plt.plot(x,y)
plt.show()