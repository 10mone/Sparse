import numpy as np
import matplotlib.pyplot as plt

def draw(x):
    t = 1
    value = []
    while t<16:
        temp_value = x[0]*(t**14)+x[1]*(t**13)+x[2]*(t**12)+x[3]*(t**11)+x[4]*(t**10)+x[5]*(t**9)+x[6]*(t**8)+x[7]*(t**7)+x[8]*(t**6)+x[9]*(t**5)+x[10]*(t**4)+x[11]*(t**3)+x[12]*(t**2)+x[13]*t+x[14]
        value.append(temp_value)
        t += 1
    return value


t = [i for i in range(1,16)]
y = []

for i in t:
    noise = np.random.normal(loc=0, scale=0.5)
    y.append(2*i+noise)

y = np.array(y)

phi = np.vander(t)
x = np.dot(np.linalg.inv(phi), y.T)

result = draw(x)

print(x)

ax = plt.subplot()
plt.plot(y,'o')
plt.plot(result)
ax.set_xlim(-2.0, 16.0)
ax.set_ylim(-2.0, 50.0)
plt.show() 
