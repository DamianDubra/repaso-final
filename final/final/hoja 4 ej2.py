# se tiene el archivo datos.txt que contiene datos de servicios meteorologicos
# dice fechasmedi, provincia,temperatura, humedad, presion
# archivo ordenado por provincia 
# mostrar cantidad mediciones por provincia, mayor temperatura, promedio temp, promedio humedad, provincia con mayor temp, prov con menor hum

varchivo=open('datos.txt','r')
vregistro=varchivo.readline().strip()
vector=vregistro.split(';')

vauxiprovmaytemp=-1.0
vprovmastemp=''
vauximenhum=9999.0
vprovmenhum=''
while vregistro!='':
    mediciones=0
    vprovincia=vector[1]
    vauxitempmaxprov=0
    vacumtemp=0
    vpromtemp=0.0
    vacumhum=0
    vpromhum=0.0
    vauximayortemp=0.0

    while vregistro!='' and vector[1]==vprovincia:
        mediciones+=1
        if vauximayortemp<int(vector[2]):
            vauximayortemp=int(vector[2])
        vacumtemp+=int(vector[2])
        vacumhum+=int(vector[3])
        vregistro=varchivo.readline().strip()
        vector=vregistro.split(';')
    vpromtemp=vacumtemp/mediciones
    vpromhum=vacumhum/mediciones
    if vauxiprovmaytemp<vpromtemp:
        vauximayortemp=vpromtemp
        vprovmastemp=vprovincia
    if vpromhum<vauximenhum:
        vauximenhum=vpromhum
        vprovmenhum=vprovincia
    print('la provincia ',vprovincia)
    print('las mediciones ',mediciones)
    print('el promedio de temp',vpromtemp)
    print('el promedio de humedad ',vpromhum)

print('la provincia con mayor prom de tem', vprovmastemp)
print('la de menor prom de hum ',vprovmenhum)

varchivo.close()