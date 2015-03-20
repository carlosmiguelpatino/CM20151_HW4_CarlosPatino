import scikits.audiolab as audio
import matplotlib.pyplot as plt
import numpy as np

#Para este codigo es necesario tener instalado scikits 
input_signal, sampling_rate, enc = audio.wavread("minombre.wav")
time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate))

fig = plt.figure()
plt.plot(time_array[0:100000], input_signal[0:100000])
plt.title("Grafica de amplitud de voz", fontsize=25)
plt.xlabel("Tiempo (s)", fontsize=15)
plt.ylabel("Amplitud", fontsize=15)
plt.savefig("mi_voz.png") #la grafica de guarda en la carpeta data