import numpy as np
import matplotlib.pyplot as plt

def draw(x):
    t = 1
    value = []
    while t<16:
        temp_value = x[0]*t + x[1] 
        value.append(temp_value)
        t += 1
    return value


t = [i for i in range(1,16)]
y = []

for i in t:
    noise = np.random.normal(loc=0, scale=0.5)
    y.append(2*i+noise)

y = np.array(y)

phi15 = np.vander(t)
phi = phi15[:,[13,14]]

x = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)), phi.T), y.T)

result = draw(x)

print(x)

ax = plt.subplot()
plt.plot(y,'o')
plt.plot(result)
ax.set_xlim(-2.0, 16.0)
ax.set_ylim(-2.0, 50.0)
plt.show() 
