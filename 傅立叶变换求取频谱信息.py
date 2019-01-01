import numpy as np
from scipy import  fftpack
import matplotlib.pyplot as plt

N = 1000
t = 1.0/200
x = np.linspace(0.0, N*t, N)
y = 6*np.sin(2*np.pi*x) + 0.2*np.cos(100*np.pi*x) + 0.03*np.sin(120*np.pi*x)
plt.figure(1)
plt.plot(x,y)
yf = fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*t), N/2)
plt.figure(2)
plt.plot(xf, 2.0//N*np.abs(yf[0:N//2]))
plt.show()