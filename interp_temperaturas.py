import numpy as np
import matplotlib.pyplot as plt
import os as os
import datetime as DT
from matplotlib.dates import date2num
from scipy.interpolate import interp1d
from scipy.interpolate import InterpolatedUnivariateSpline
import csv

#Creacion de vectores de datos por ciudades

filename = './data/temperaturas.csv'
dbog, dcali, dbquilla, dbucmng, dipi = [], [], [], [], []
tbog, tcali, tbquilla, tbucmng, tipi = [], [], [], [], []
with open(filename) as f:    
    reader = csv.reader(f)     
    next(reader)
    for row in reader:
        if row[4] != "NA":
            if row[3] == "Bogota":
                tbog.append(float(row[4]))
                dbog.append(str(row[2]))
            if row[3] == "Cali":
                tcali.append(float(row[4]))
                dcali.append(str(row[2]))
            if row[3] == "Barranquilla":
                tbquilla.append(float(row[4]))
                dbquilla.append(str(row[2]))
            if row[3] == "Bucaramanga":
                tbucmng.append(float(row[4]))
                dbucmng.append(str(row[2]))
            if row[3] == "Ipiales":
                tipi.append(float(row[4]))
                dipi.append(str(row[2]))

#Conversion a formato de fecha
fechas = []
for i in range(len(dbog)):
    date = DT.datetime.strptime(dbog[i], "%Y-%m-%d")
    fechas.append(date)    
dbog = fechas    
    
fechas = []
for i in range(len(dcali)):
    date = DT.datetime.strptime(dcali[i], "%Y-%m-%d")
    fechas.append(date)
dcali = fechas

fechas = []
for i in range(len(dbquilla)):
    date = DT.datetime.strptime(dbquilla[i], "%Y-%m-%d")
    fechas.append(date)
dbquilla = fechas

fechas = []
for i in range(len(dbucmng)):
    date = DT.datetime.strptime(dbucmng[i], "%Y-%m-%d")
    fechas.append(date)
dbucmng = fechas

fechas = []
for i in range(len(dipi)):
    date = DT.datetime.strptime(dipi[i], "%Y-%m-%d")
    fechas.append(date)
dipi = fechas


#Graficos de interpolaciones Bogota
x = date2num(dbog)
x_test = np.linspace(x[0], x[-1], 1000)

fit2 = np.polyfit(x, tbog, 2)

f = interp1d (x, tbog)

spline = InterpolatedUnivariateSpline(x, tbog)

print spline(x_test)


plt.plot(x, fit2[0]*x**2 + fit2[1]*x + fit2[2], color = 'r')
plt.plot(x_test,f(x_test), color = 'b')
plt.plot(x_test, spline(x_test), color = 'g')
plt.scatter(x, tbog, c='k')
plt.legend(['Polinomio', 'Interp1d', 'Splines' ,'data'])
plt.show()

#Graficos de interpolaciones Cali
x = date2num(dcali)
x_test = np.linspace(x[0], x[-1], 1000)

fit2 = np.polyfit(x, tcali, 2)

f = interp1d (x, tcali)

spline = InterpolatedUnivariateSpline(x, tcali)


plt.plot(x, fit2[0]*x**2 + fit2[1]*x + fit2[2], color = 'r')
plt.plot(x_test,f(x_test), color = 'b')
plt.plot(x_test, spline(x_test), color = 'g')
plt.scatter(x, tcali, c='k')
plt.legend(['Polinomio', 'Interp1d', 'Splines' ,'data'])
plt.show()

#Graficos de interpolaciones Barranquilla
x = date2num(dbquilla)
x_test = np.linspace(x[0], x[-1], 1000)

fit2 = np.polyfit(x, tbquilla, 2)

f = interp1d (x, tbquilla)

spline = InterpolatedUnivariateSpline(x, tbquilla)


plt.plot(x, fit2[0]*x**2 + fit2[1]*x + fit2[2], color = 'r')
plt.plot(x_test,f(x_test), color = 'b')
plt.plot(x_test, spline(x_test), color = 'g')
plt.scatter(x, tbquilla, c='k')
plt.legend(['Polinomio', 'Interp1d', 'Splines' ,'data'])
plt.show()

#Graficos de interpolaciones Bucaramanga
x = date2num(dbucmng)
x_test = np.linspace(x[0], x[-1], 1000)

fit2 = np.polyfit(x, tbucmng, 2)

f = interp1d (x, tbucmng)

spline = InterpolatedUnivariateSpline(x, tbucmng)


plt.plot(x, fit2[0]*x**2 + fit2[1]*x + fit2[2], color = 'r')
plt.plot(x_test,f(x_test), color = 'b')
plt.plot(x_test, spline(x_test), color = 'g')
plt.scatter(x, tbucmng, c='k')
plt.legend(['Polinomio', 'Interp1d', 'Splines' ,'data'])
plt.show()

#Graficos de interpolaciones Ipiales
x = date2num(dipi)
x_test = np.linspace(x[0], x[-1], 1000)

fit2 = np.polyfit(x, tipi, 2)

f = interp1d (x, tipi)

spline = InterpolatedUnivariateSpline(x, tipi)


plt.plot(x, fit2[0]*x**2 + fit2[1]*x + fit2[2], color = 'r')
plt.plot(x_test,f(x_test), color = 'b')
plt.plot(x_test, spline(x_test), color = 'g')
plt.scatter(x, tipi, c='k')
plt.legend(['Polinomio', 'Interp1d', 'Splines' ,'data'])
plt.show()

#Calculo del error

# def least_squares(y_data, y_calculada):
# 	a = 0
#     for i in range (len(y_data)):
#         a = a + (y_data[i] - y_calculada[i])**2
        
#     return a

# y_calculada = []
# for i in range(len(x)):
#     y_calculada.append(fit2[0]*x[i]**2 + fit2[1]*x[i] + fit2[2])

# y_calculada = []
# for i in range(len(x)):
#     y_calculada.append(fit2[0]*x[i]**2 + fit2[1]*x[i] + fit2[2])

# print "Error cuadratico para polinomio", least_squares(tbog, y_calculada)

