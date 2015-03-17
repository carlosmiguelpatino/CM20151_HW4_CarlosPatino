library(tidyr)
library(dplyr)
library(lubridate)
library(ggplot2)

#Descarga de datos por ciudad
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802220000_13_0/station.txt', destfile = 'bogota.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305802590000_13_0/station.txt', destfile = 'cali.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800940000_13_0/station.txt', destfile = 'bucaramanga.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305800280000_13_0/station.txt', destfile = 'barranquilla.txt', method = 'wget')
download.file('http://data.giss.nasa.gov/tmp/gistemp/STATIONS/tmp_305803700000_13_0/station.txt', destfile = 'ipiales.txt', method = 'wget')


#Importacion de datos a data frames
bogota = read.table("bogota.txt", header = TRUE)
cali = read.table("cali.txt", header = TRUE)
bucaramanga = read.table("bucaramanga.txt", header = TRUE)
barranquilla = read.table("barranquilla.txt", header = TRUE)
ipiales = read.table("ipiales.txt", header = TRUE)

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
bogota <- mutate(bogota, fecha = paste(año, MesNum(mes), "1", sep="/"))
bogota <- mutate(bogota, ciudad = "Bogota")
cali <- mutate(cali, fecha = paste(año, MesNum(mes), "1", sep="/"))
cali <- mutate(cali, ciudad = "Cali")
bucaramanga <- mutate(bucaramanga, fecha = paste(año, MesNum(mes), "1", sep="/"))
bucaramanga <- mutate(bucaramanga, ciudad = "Bucaramanga")
barranquilla <- mutate(barranquilla, fecha = paste(año, MesNum(mes), "1", sep="/"))
barranquilla <- mutate(barranquilla, ciudad = "Barranquilla")
ipiales <- mutate(ipiales, fecha = paste(año, MesNum(mes), "1", sep="/"))
ipiales <- mutate(ipiales, ciudad = "Ipiales")

temperaturas <- rbind(bogota, cali, bucaramanga, barranquilla, ipiales)

temperaturas <- temperaturas[c("año", "mes", "fecha", "ciudad", "temperatura")]
temperaturas[temperaturas == 999.9] <- NA

write.csv(temperaturas, file = "temperaturas.csv")

#Crear grafica
grafica <- ggplot(temperaturas, aes(x = fecha, y = temperatura)) + geom_line() + geom_point() + ggtitle("Temperatura en Colombia \n 1961-2015") + facet_wrap(~ ciudad, scales = "free")
ggsave(filename='temperaturas.png', plot = grafica)
