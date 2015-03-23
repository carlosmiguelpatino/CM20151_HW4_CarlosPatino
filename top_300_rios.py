import os
import numpy as np
import pandas as pd

#Descarga del archivo a carpeta data
os.system("wget -P ./data http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt")

#Limpieza de archivo
f = open('./data/coastal-stns-byVol-updated-oct2007.txt', 'r')
f_new = open('./data/tmp_file.csv', 'w')

for line in f:
    line = str(line)
    line = line.split()
    line[14:] = [''.join(line[14:])]
    columna = line[0]
    for i in range(1,len(line)):
        columna = columna + " " + line[i]        
    f_new.write(columna + '\n')
f.close()


mydata = pd.read_table("./data/tmp_file.csv",sep=" ")
mydata = mydata.sort(['Vol(km3/yr)'], ascending=False)
mydata.head()

final_data = mydata[0:300]
final_data.to_csv("./data/top_300_rios.csv", sep=',', index=False)

os.system("rm ./data/tmp_file.csv" )
