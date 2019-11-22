import math
import numpy as np
import matplotlib.pyplot as plt

def draw(x):
    tt = 0
    result_value = []
    true_value = []
    while tt<10.1:
        temp_value = x[0]*(tt**6) + x[1]*(tt**5) + x[2]*(tt**4) + x[3]*(tt**3) + x[4]*(tt**2) + x[5]*tt + x[6]
        #temp_value = x[0]*(tt**10)+x[1]*(tt**9)+x[2]*(tt**8)+x[3]*(tt**7)+x[4]*(tt**6)+x[5]*(tt**5)+x[6]*(tt**4)+x[7]*(tt**3)+x[8]*(tt**2)+x[9]*tt+x[10]

        result_value.append(temp_value)
        true_value.append(math.sin(tt))
        tt += 0.1
    return result_value, true_value

t = [i for i in range(0,11)]
y = []
true_value = []

for i in t:
    noise = np.random.normal(loc=0, scale=0.2)
    y.append(math.sin(i)+noise)

#used to dot the noise values
yy = [None for _ in range(101)]
for i in range(0,11):
    yy[i*10] = y[i]

t = np.array(t)
y = np.array(y)

phi15 = np.vander(t)
phi = phi15[:,[4, 5, 6, 7, 8, 9, 10]]

x = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)),phi.T),y.T)
print(x)
result, true_value = draw(x)


ax = plt.subplot()
plt.plot(yy,'o', color='blue', label='noise data')
plt.plot(result, color='blue', label='calculated value')
plt.plot(true_value, color='red', linestyle='dashed', label='true value')
plt.legend()
ax.set_xticks(np.linspace(0, 100, 11))
ax.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10'])

ax.set_xlim(0.0, 100.0)
ax.set_ylim(-2.0, 2.0)
plt.title('Figure2-7 6dim')
plt.show()

