import numpy as np
import matplotlib.pyplot as plt

piano=np.loadtxt("ps8/piano.txt")
plt.plot(0)
plt.plot(piano)
n=9
custom_units_time = np.linspace(0,1,num=n)*100000
plt.xticks(custom_units_time, np.round(np.linspace(0,1,num=n)*100000/44100,decimals=1))
plt.xlabel("time(s)")
plt.title('Piano Amplitude')
piano_freq=np.fft.rfft(piano)
plt.show(1)

custom_units_freq = np.linspace(0,1,num=n)*5000
plt.xticks(custom_units_freq, np.int32(np.linspace(0,1,num=n)*22050*.1))
plt.xlabel("Frequency(Hz)")
plt.title('Piano Spectrum')
plt.plot(np.abs(piano_freq)[:5000])
#22050 is nyquist and corresponds to last element in array

np.where(piano_freq==np.max(piano_freq))[0]*(22050/50000)