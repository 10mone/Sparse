import numpy as np
import matplotlib.pyplot as plt

def drawing(yy, result, true_value, t_message):
    ax = plt.subplot()
    plt.plot(yy,'o', color='blue', label='noise data')
    plt.plot(result, color='blue', label='calculated value')
    plt.plot(true_value, color='red', linestyle='dashed', label='true value')
    plt.legend()

    #change the x-axis-label (not change the value itself) 
    ax.set_xticks(np.linspace(0, 100, 11))
    ax.set_xticklabels(['0','1','2','3','4','5','6','7','8','9','10'])

    ax.set_xlim(0.0, 100.0)
    ax.set_ylim(-2.0, 2.0)
    plt.title(t_message)
    plt.show()
