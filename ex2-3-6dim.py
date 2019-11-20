import math
import numpy as np
import matplotlib.pyplot as plt

def draw(x):
    t = 0
    value = []
    while t<11:
        temp_value = x[0]*(t**6)+x[1]*(t**5)+x[2]*(t**4)+x[3]*(t**3)+x[4]*(t**2)+x[5]*t+x[6]
        value.append(temp_value)
        t += 1
    return value


t = [i for i in range(0,11)]
y = []
line = []

for i in t:
    noise = np.random.normal(loc=0, scale=0.2)
    y.append(math.sin(i)+noise)
    line.append(math.sin(i))

t = np.array(t)
y = np.array(y)

phi15 = np.vander(t)
phi = phi15[:,[0, 1, 2, 3, 4, 5, 6]]

x = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)),phi.T),y.T)

result = draw(x)
print()
print(x)
ax = plt.subplot()
plt.plot(result, color='blue')
plt.plot(line, color='red', linestyle='dashed')
plt.plot(y, color='blue', marker='o')
ax.set_xlim(0.0, 10.0)
ax.set_ylim(-2.0, 2.0)
plt.show()


