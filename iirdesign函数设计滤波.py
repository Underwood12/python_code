import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N = 1000
t = 1.0/200
x = np.linspace(0.0, N*t, N)
y = 6*np.sin(2*np.pi*x) + 0.2*np.cos(100*np.pi*x) + 0.03*np.sin(120*np.pi*x)
b, a = signal.iirdesign(0.05, 0.2, 2, 10)
z = signal.lfilter(b, a, y)
plt.plot(x, y, 'g')
plt.plot(x, z, 'r')
plt.show()
