# crear un programa con el archivo socios.txt, que tiene nrosocio, apellido, nombre,edad,sexo, peso ordenado por edad
#mostrar hombresxedad mujeres x edad promedio de pesso por edad, apellido de person con nro de socio mas alto por edad

varchivo=open('socios.txt','r')
vector=['']*6
vregistro=varchivo.readline().rstrip()

while vregistro!='':
    vector=vregistro.split(';')
    vedad=int(vector[3])
    hombres=0
    mujer=0
    acumpesohom=0.0
    promediohom=0.0
    acumpesomuj=0.0
    promediomuj=0.0
    vauxilegajo=0
    vapellidoauxi=''
    vauxiedad=vedad
    while vregistro!='' and vauxiedad==vedad:
        vauxiedad=int(vector[3])
        if vector[4]=='h':
            hombres+=1
            acumpesohom+=float(vector[5])
        else:
            mujer+=1
            acumpesomuj+=float(vector[5])

        if int(vector[0])>vauxilegajo:
            vauxilegajo=int(vector[0])
            vapellidoauxi=vector[1]
        vregistro=varchivo.readline().strip()
        vector=vregistro.split(';')
    if hombres!=0:
        promediohom=acumpesohom/hombres
    if mujer!=0:
        promediomuj=acumpesomuj/mujer

    print('la cnatidad de hombres con edad',vedad,'es',hombres,'el peso promedio',promediohom)
    print('la cnatidad de mujeres con edad',vedad,'es',mujer,'el peso promedio',promediomuj)
    print('el legajo', vauxilegajo,'apellido: ',vapellidoauxi)
    varchivo.close()
    