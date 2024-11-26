# tengo un archivo empleandos.txt tiene legajo, apellido, sector y sueldo ordenado por sector
# mostrar cantidad empleado por sector total sueldos por sector nombre sector con mas personas

varchivo=open('empleados.txt','r')
vregistro=varchivo.readline().strip()
vector=['']*4
vector=vregistro.split(';')

while vregistro!='':
    vsector=vector[2]
    empleados=0
    vauximasempl=0
    sectormasempl=''
    acumsuel=0
    while vregistro!='' and vector[2]==vsector:
        empleados+=1
        acumsuel+=int(vector[3])
        vregistro=varchivo.readline().strip()
        vector=vregistro.split(';')
    if empleados>vauximasempl:
        vauximasempl=empleados
        sectormasempl=vsector
    print('los empledos del sector: ',vsector,'son en total', empleados)
    print('el sueldo total es', acumsuel)

print('el sector',sectormasempl,'es el que mas empleados tiene')
varchivo.close()