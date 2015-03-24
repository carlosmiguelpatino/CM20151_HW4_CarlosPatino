# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os as os
import datetime as DT
from matplotlib.dates import date2num
from scipy.interpolate import interp1d, InterpolatedUnivariateSpline, KroghInterpolator
from scipy.stats import chisquare
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
def conversion_formato(dciudad):
    fechas = []
    for i in range(len(dciudad)):
        date = DT.datetime.strptime(dciudad[i], "%Y-%m-%d")
        fechas.append(date)    
    return fechas    
 

dbog = conversion_formato(dbog)
dcali = conversion_formato(dcali)
dbquilla = conversion_formato(dbquilla)
dbucmng = conversion_formato(dbucmng)
dipi = conversion_formato(dipi)


#Para hacer interpolacion con splines el valor de x debe ir en aumento
def ordenar(dciudad, tciudad):
    dciudad = date2num(dciudad)  
    dciudad, tciudad = (list(t) for t in zip(*sorted(zip(dciudad, tciudad))))

    return (dciudad, tciudad)

dbog, tbog = ordenar(dbog,tbog)
dcali, tcali = ordenar(dcali,tcali)
dbquilla, tbquilla = ordenar(dbquilla,tbquilla)
dbucmng, tbucmng = ordenar(dbucmng,tbucmng)
dipi, tipi = ordenar(dipi, tipi)

#Calculo del error
def calculo_error(t_true, t_pol, t_spline, t_lin, ciudad):
    chi_pol = chisquare(t_pol, t_true)
    chi_spline = chisquare(t_spline, t_true)
    chi_lin = chisquare(t_lin, t_true)

    if chi_pol < chi_lin and chi_pol < chi_spline:
        print "Para " + ciudad + " resulta mejor la interpolacion polinomica"

    if chi_lin < chi_pol and chi_lin < chi_spline:
        print "Para " + ciudad + " resulta mejor la interpolacion lineal"

    if chi_spline < chi_lin and chi_spline < chi_pol:
        print "Para " + ciudad + " resulta mejor la interpolacion por splines"



#Graficos interpolaciones

def crear_interpolaciones(dciudad, tciudad, ciudad):
    x = dciudad  
    x_test = np.linspace(x[0], x[-1], 3000)
    
    fit5 = np.polyfit(x, tciudad, 5) #Interpolacion polinomio de grado cinco. Se escogio este grado de polinomio porque al hacer la pruebas es el que mejor se ajusta a los crecimientos y decrecimientos de la tempratura. Sin embargo no resulta practico usar polinomios de mayor grado ya que nunca se va a poder llegar a una concordoncia completa para todos los puntos

    f_1 = interp1d (x, tciudad) #Interpolacion lineal

    spline = InterpolatedUnivariateSpline(x, tciudad, k=3) #Interpolacion por splines

    #Mensaje de mejor interpolacion
    calculo_error(tciudad, (fit5[0]*np.asarray(x)**5 + fit5[1]*np.asarray(x)**4 + fit5[2]*np.asarray(x)**3 + fit5[3]*np.asarray(x)**2 + fit5[4]*np.asarray(x) + fit5[5]), spline(x), f_1(x), ciudad) 

    fig = plt.figure()

    plt.title('Temperatura de ' + ciudad)

    plt.subplot(3,1,1)
    plt.plot(x_test, fit5[0]*x_test**5 + fit5[1]*x_test**4 + fit5[2]*x_test**3 + fit5[3]*x_test**2 + fit5[4]*x_test + fit5[5] , color = 'r') 
    plt.scatter(x, tciudad, c='k')
    plt.legend(['Polinomio','data'])

    plt.subplot(3,1,2)
    plt.plot(x_test,f_1(x_test), color = 'b')
    plt.scatter(x, tciudad, c='k')
    plt.legend(['Interp1d','data'])

    plt.subplot(3,1,3)
    plt.plot(x_test, spline(x_test), color = 'g')  
    plt.scatter(x, tciudad, c='k')
    plt.legend(['Splines' ,'data'])

    
    plt.savefig('./data/temp_'+ciudad+'.png')


crear_interpolaciones(dbog,tbog,"Bogota")
crear_interpolaciones(dcali,tcali,"Cali")
crear_interpolaciones(dbquilla,tbquilla,"Barranquilla")
crear_interpolaciones(dbucmng,tbucmng,"Bucaramanga")
crear_interpolaciones(dipi,tipi, "Ipiales")


