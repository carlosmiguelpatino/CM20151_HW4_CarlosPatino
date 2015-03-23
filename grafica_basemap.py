#La grafica se demora un poco en generar porque es necesario que salga en gran tamanio para poder apreciar los caudales

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv

filename = './data/top_300_rios.csv'

fig = plt.figure(figsize = (48, 36))

lats, lons, caudal = [], [], []

with open(filename) as f:
    
    reader = csv.reader(f)
    
    
    next(reader)   
    
    
    for row in reader:
        lats.append(float(row[3]))
        lons.append(float(row[2]))
        caudal.append(float(row[5]))

lats = lats[:150]
lons = lons[:150]
caudal = caudal[:150]
    
fig = plt.figure(figsize=(24.0, 15.0))

map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0, lat_0=0, lon_0=-130)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'orange')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

for lon, lat,cdl in zip(lons, lats, caudal):
   x,y = map(lon, lat)
   map.plot(x, y)
   plt.text(x,y,cdl, fontsize= 7)

plt.title('Caudal de los 150 rios principales \n (en m3/year)', fontsize = 20)
plt.savefig("./data/top_rios.png") #Esta es la grafica que pide el enunciado, sin embargo me parece  mas conveniente hacer un plot que no de el caudal exacto pero si muestre mejor el caudal de los rios en la zona
