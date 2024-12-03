# se tiene un archivo con las ventas diarias por sucursales ventas.txt esta formado por
#sucursal,importe, fecha, dd/mm/aaaaa un registro por venta, sucursal entre 1 y 45,
#mostrar cna ventas por sucursal, importe total por sucursal, importe por mes nro de mes con mayor mes

#no se si esta ordenado, pero asumo que si asi practico mas rapido, por sucursal

#le agrego cargar datos
#varchivo1=open('ventas.txt','w')

#cargar=input('cargar datos')

#while cargar!='no':
  #  sucursal=input('sucursal')
 #   fecha=input('fecha dd/mm/aa')
 #   importe=input('importe')
 #   vregistro1= sucursal +';'+importe+';'+fecha
 #   varchivo1.write(vregistro1)
  #  varchivo1.write('\n')
  #  cargar=input('cargar datos')

#varchivo1.close()

varchivo=open('ventas.txt','r')
vregistro=varchivo.readline().strip()
vector=vregistro.split(';')
vectormes=[0]*12
vauximayormes=0
vnrodemes=0

while vregistro!='':
    vsucursal=vector[0]
    cantidadvent=0
    acumimp=0
    while vregistro!='' and vsucursal==vector[0]:
        cantidadvent+=1
        acumimp+=int(vector[1])
        vectornromes=vector[2].split('/')
        vectormes[int(vectornromes[1])-1]+=int(vector[1])
        vregistro=varchivo.readline().strip()
        vector=vregistro.split(';')
    print('las ventas de la sucursal',vsucursal,'es ',cantidadvent)
    print('las cantidad de ',vsucursal,'es ',acumimp)

for c in range(0,12):
    if vauximayormes<vectormes[c]:
        vauximayormes=vectormes[c]
        vnrodemes=c+1

for c in range(0,12):
    print('el mes nro',c+1,'vendio',vectormes[c])

print('el mes que mas vendio', vnrodemes,'con todoal ',vauximayormes)
