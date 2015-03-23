#Este script se debe ejecutar en la carpeta CM20151_HW4_CarlosPatino con el comando
#Rscript tablaygraficas.R
#Los resultados se almacenan en la carpeta data

library(tidyr)
library(dplyr)
library(lubridate)
library(ggplot2)

#Descarga de datos por ciudad
#Debido a que la pagina de la nasa tiene un link dinamico, es necesario actualizar el link con frecuencia.
#Es por esto que estos links funcionaron en un momento para la descarga de los archivos
#pero es probable que no funcionen luego. Por lo anterior, se incluyen los archivos necesarios
#en la carpeta data incluido en el repositorio cuyo formato. Los archivos deben estar en el
#workspace en donde se está ejecutando el archivo tablaygrafica.R
#Por lo anterior las líneas de código que descargan los archivos se dejan comentadas a continuación

#download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_13_0/station.txt', destfile = 'bogota.txt', method = 'wget')
#download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_13_0/station.txt', destfile = 'cali.txt', method = 'wget')
#download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_13_0/station.txt', destfile = 'bucaramanga.txt', method = 'wget')
#download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_13_0/station.txt', destfile = 'barranquilla.txt', method = 'wget')
#download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_13_0/station.txt', destfile = 'ipiales.txt', method = 'wget')


#Importacion de datos a data frames
bogota = read.table("./data/bogota.txt", header = TRUE)
cali = read.table("./data/cali.txt", header = TRUE)
bucaramanga = read.table("./data/bucaramanga.txt", header = TRUE)
barranquilla = read.table("./data/barranquilla.txt", header = TRUE)
ipiales = read.table("./data/ipiales.txt", header = TRUE)

#Limpieza y organizacion de data frames
keeps <- c("año","mes", "temperatura")

bogota <- gather(bogota, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(bogota)[1] <- "año"
bogota <- bogota[,keeps,drop=FALSE]

cali <- gather(cali, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(cali)[1] <- "año"
cali <- cali[,keeps,drop=FALSE]

bucaramanga <- gather(bucaramanga, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(bucaramanga)[1] <- "año"
bucaramanga <- bucaramanga[,keeps,drop=FALSE]

barranquilla <- gather(barranquilla, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(barranquilla)[1] <- "año"
barranquilla <- barranquilla[,keeps,drop=FALSE]

ipiales <- gather(ipiales, mes, temperatura, JAN:DEC, na.rm = TRUE)
names(ipiales)[1] <- "año"
ipiales <- ipiales[,keeps,drop=FALSE]

#Adicion columnas faltantes
MesNum <- function(x) match(tolower(x), tolower(month.abb))
bogota <- mutate(bogota, fecha = as.Date(paste("1", MesNum(mes),  año, sep="-"), "%d-%m-%Y"))
bogota <- mutate(bogota, ciudad = "Bogota")
cali <- mutate(cali, fecha = as.Date(paste("1", MesNum(mes),  año, sep="-"), "%d-%m-%Y"))
cali <- mutate(cali, ciudad = "Cali")
bucaramanga <- mutate(bucaramanga, fecha = as.Date(paste("1", MesNum(mes),  año, sep="-"), "%d-%m-%Y"))
bucaramanga <- mutate(bucaramanga, ciudad = "Bucaramanga")
barranquilla <- mutate(barranquilla, fecha = as.Date(paste("1", MesNum(mes),  año, sep="-"), "%d-%m-%Y"))
barranquilla <- mutate(barranquilla, ciudad = "Barranquilla")
ipiales <- mutate(ipiales, fecha = as.Date(paste("1", MesNum(mes),  año, sep="-"), "%d-%m-%Y"))
ipiales <- mutate(ipiales, ciudad = "Ipiales")

temperaturas <- rbind(bogota, cali, bucaramanga, barranquilla, ipiales)

temperaturas <- temperaturas[c("año", "mes", "fecha", "ciudad", "temperatura")]
temperaturas[temperaturas == 999.9] <- NA

write.csv(temperaturas, file = "./data/temperaturas.csv", row.names = FALSE)



#Crear grafica
png("temperaturas.png",height=800,width=1600)
grafica <- ggplot(temperaturas, aes(x = fecha, y = temperatura, group = 1))+ geom_point(size = 1) + ggtitle("Temperatura en Colombia \n 1961-2015") + facet_wrap(~ ciudad, scales = "free") + geom_line() + ylab("Temperatura (°C)") + xlab("Fecha")
ggsave(filename='./data/temperaturas.png', plot = grafica)
