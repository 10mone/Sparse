import numpy as np
import matplotlib.pyplot as plt

def draw(x):
    tt = 1
    result_value = []
    true_value = []
    while tt<16:
        temp_value = x[0]*(tt**14)+x[1]*(tt**13)+x[2]*(tt**12)+x[3]*(tt**11)+x[4]*(tt**10)+x[5]*(tt**9)+x[6]*(tt**8)+x[7]*(tt**7)+x[8]*(tt**6)+x[9]*(tt**5)+x[10]*(tt**4)+x[11]*(tt**3)+x[12]*(tt**2)+x[13]*tt+x[14]
        result_value.append(temp_value)
        true_value.append(2*tt)
        tt += 0.1
    return result_value, true_value


t = [i for i in range(1,16)]
y = []
true_value = []

for i in t:
    noise = np.random.normal(loc=0, scale=0.5)
    y.append(2*i+noise)

#used to dot the noise values
yy = [None for _ in range(151)]
for i in range(0,15):
    yy[i*10] = y[i]

y = np.array(y)

phi = np.vander(t)
x = np.dot(np.linalg.inv(phi), y.T)

result,true_value = draw(x)

ax = plt.subplot()


plt.plot(yy, 'o', color='blue', label='noise data')
plt.plot(result, color='blue', label='calculated value')
plt.plot(true_value, color='red', linestyle='dashed', label='true value')
plt.legend()
ax.set_xticks(np.linspace(0, 150, 4))
ax.set_xticklabels(['0','5','10','15'])

ax.set_xlim(0.0, 150.0)
ax.set_ylim(0.0, 50.0)
plt.show() 
