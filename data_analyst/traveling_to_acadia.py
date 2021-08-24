# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(flights,range=(0,365),bins=365);plt.xlabel('day');plt.ylabel('flights');plt.title('flights by day')
plt.subplot(212)
plt.hist(in_bloom,bins=365);plt.xlabel('day');plt.ylabel('blooms');plt.title('flower blooms by day')
plt.tight_layout()
plt.show()
