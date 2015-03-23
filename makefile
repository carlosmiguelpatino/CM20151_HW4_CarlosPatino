all: mi_voz.png mi_voz_fft.png

mi_voz_fft.png: minombre.wav fft_de_mi_voz.py
	python fft_de_mi_voz.py

mi_voz.png: minombre.wav grafica_mi_voz.py
	python grafica_mi_voz.py

minombre.wav: a.out
	./a.out

a.out: grabar_mi_nombre.c
	gcc grabar_mi_nombre.c

 

