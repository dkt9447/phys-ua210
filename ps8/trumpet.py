import numpy as np
import matplotlib.pyplot as plt

trumpet=np.loadtxt("ps8/trumpet.txt")
plt.plot(0)
plt.plot(trumpet)
n=9
custom_units_time = np.linspace(0,1,num=n)*100000
plt.xticks(custom_units_time, np.round(np.linspace(0,1,num=n)*100000/44100,decimals=1))
plt.xlabel("time(s)")
plt.title('trumpet Amplitude')
trumpet_freq=np.fft.rfft(trumpet)
plt.show(1)

custom_units_freq = np.linspace(0,1,num=n)*10000
plt.xticks(custom_units_freq, np.int32(np.linspace(0,1,num=n)*22050*.2))
plt.xlabel("Frequency(Hz)")
plt.title('trumpet Spectrum')
plt.plot(np.abs(trumpet_freq)[:10000])
#22050 is nyquist and corresponds to last element in array
np.where(trumpet_freq==np.max(trumpet_freq))[0]*(22050/50000)