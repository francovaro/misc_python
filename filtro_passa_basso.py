from matplotlib import pyplot as plt
import numpy as np

c = 10e-6
r = 10e3

freq = np.arange(0, 1000, 0.01)
yp = (1/(1+c*r*freq*2*3.14))

plt.plot(freq, yp, "g")

#plt.yscale('log')
plt.xscale('log')

plt.grid(True)
plt.show()