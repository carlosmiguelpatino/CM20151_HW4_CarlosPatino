from scipy.fftpack import fft, fftfreq
import scikits.audiolab as audio
import matplotlib.pyplot as plt
import numpy as np

input_signal, sampling_rate, enc = audio.wavread("minombre.wav")
time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate))

n = len(time_array[0:100000])
f = 200.0 
dt = 1 / (f * n/7. ) 
fft_x = fft(input_signal[0:100000])
freq = fftfreq(n, dt)

#Creacion de la grafica
fig = plt.figure()
grafica = plt.plot(freq,abs(fft_x))
plt.title("Espectro de frecuencias", fontsize=25)
plt.xlabel("Frecuencia", fontsize=15)
plt.savefig("mivoz_fft.png")

#Armonicos
'''
Para encontrar los armonicos se toman los valores de frecuencia y del valor absoluto de la transformada rapida de fourier. Estos valores se toman
de tal manera que el valor de fft_x en la lista le corresponda al de la grafica. Posteriormente se ordenan los fft_x para encontrar lo valores maximos. 
Como se sabe que habra un pico en la frecuencia 0, el segundo valor de fft_x para encontrar el maximo armonico. Con el valor de fft_x, se encuentra
recupera el indice de este valor en la lista y se busca con ese indice el valor de la frecuencia.
'''
fft_x_ordenados =  sorted(abs(fft_x), reverse = True)
valores_x = grafica[0].get_xdata()
valores_y = grafica[0].get_ydata()
idx = np.where(valores_y==fft_x_ordenados[1])
print "El mayor armonico es",valores_x[idx][0]  







