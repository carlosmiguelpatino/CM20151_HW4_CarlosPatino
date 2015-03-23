import datetime as dt 
import numpy as np
from netCDF4 import Dataset 
import  mpl_toolkits.basemap 
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

f = Dataset("./data/air.mon.ltm.nc", mode='r')
fig = plt.figure()

air = f.variables['air']
lat = f.variables['lat'][:]
lon = f.variables['lon'][:]

lon1 = lon.copy()
for n, l in enumerate(lon1):
    if l >= 180:
       lon1[n]=lon1[n]-360. 
lon = lon1

air1 = air[:,0:72]
air2 = air[:,72:]
lon1 = lon[0:72]
lon2 = lon[72:]

air_new = np.hstack((air2, air1))
lon_new = np.hstack((lon2, lon1))
air_new = np.flipud(air_new)
lat_new = np.flipud(lat)


lon2, lat2 = np.meshgrid(lon,lat)
lon_0 = lon.mean()
lat_0 = lat.mean()
m =Basemap(projection='moll', llcrnrlat=-90, urcrnrlat=90,\
            llcrnrlon=0, urcrnrlon=360, resolution='c', lon_0=0)

x, y = m(lon2, lat2)

m.drawcoastlines()
m.contourf(x,y,air[0,:,:])

cbar = m.colorbar()
cbar.set_label('C')
plt.title('Temperatura media de la Tierra', fontsize  = 20)
plt.savefig("./data/grf_sin_interp.png")

#Grafica con interpolacion

fig  = plt.figure()

lon1 = lon.copy()
for n, l in enumerate(lon1):
    if l >= 180:
       lon1[n]=lon1[n]-360. 
lon = lon1

air1 = air[:,0:72]
air2 = air[:,72:]
lon1 = lon[0:72]
lon2 = lon[72:]

air_new = np.hstack((air2, air1))
lon_new = np.hstack((lon2, lon1))
air_new = np.flipud(air_new)
lat_new = np.flipud(lat)

#Esto es equivalente a hacer una interpolacion nearest neighbors
air_cyclic, lons_cyclic = addcyclic(air_new[0, :, :], lon_new)


m =Basemap(projection='moll', llcrnrlat=-90, urcrnrlat=90,\
            llcrnrlon=0, urcrnrlon=360, resolution='c', lon_0=0)


lon2, lat2 = np.meshgrid(lon_new,lat_new)

x, y = m(lon2, lat2)

m.drawcoastlines()
m.contourf(x,y,air[0,:,:])

cbar = m.colorbar()
cbar.set_label('C')
plt.title('Temperatura media de la Tierra \n con interpolacion', fontsize = 20)
plt.savefig("./data/grf_con_interp.png")

'''
Con la interpolacion nearest neighbors se logra completar la grafica donde no hay datos disponibles
'''



