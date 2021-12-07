from matplotlib import pyplot as plt
import numpy as np
import sys, getopt

arguments = sys.argv[1:]
shortopts = "rcp"
longopts = ["f_start=", "f_stop="]

c       = 10e-6
r       = 10e3
f_start = 0
f_stop  = 10e3

try:
    # Printing different options and arguments
    options, args = getopt.getopt(arguments, shortopts, longopts)
except getopt.GetoptError:   
        sys.exit(2)

for opt, val in options:
    if opt in ("-r"):
        r = r
    if opt in ("-c"):
        c = c
    if opt in ("-p"):
        c = c
    if opt in ("--f_start"):
        f_start = val
    if opt in ("--f_stop"):
        f_stop = val

print("Test of high pass filter")
print("C = " + str(c) + " F")
print("R = " + str(r) + " Ohm")
print("F start = " + str(f_start) + " Hertz")
print("F stop = " + str(f_stop) + " Hertz")

freq = np.arange(f_start, f_stop, 0.01)
yp = ((r*c*freq*2*3.14)/(1+c*r*freq*2*3.14))

plt.plot(freq, yp, "g")

#plt.yscale('log')
plt.xscale('log')

plt.grid(True)
plt.show()
