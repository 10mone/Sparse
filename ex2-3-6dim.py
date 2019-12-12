import math
import numpy as np
import matplotlib.pyplot as plt
from drawing import drawing

def calc(x):
    tt = 0
    result_value = []
    true_value = []
    while tt<10.1:
        temp_value = x[0]*(tt**6) + x[1]*(tt**5) + x[2]*(tt**4) + x[3]*(tt**3) + x[4]*(tt**2) + x[5]*tt + x[6]
        
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
result, true_value = calc(x)

drawing(yy, result, true_value, '6dim')

