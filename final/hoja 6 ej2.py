#se tiene un archivo llamado empleado.txt , dice legajo,apell,sector,sueldo y sexo
#ordenado por sector de trabajo
#mostar cant pers por secto, cant m por sex, total sueld,sector con mas persona

varchivo=open('empleado.txt','r')
vregistro=varchivo.readline().strip()
vector=vregistro.split(';')

vauxmasper=0
vsecmasper=''

while vregistro!='':
    vsecto=vector[2]
    cantper=0
    cantm=0
    acumsueld=0
    while vregistro!='' and vector[2]==vsecto:
        cantper+=1
        if vector[4]=='m':
            cantm+=1
        acumsueld+=float(vector[3])
        vregistro=varchivo.readline().strip()
        vector=vregistro.split(';')

    if cantper>vauxmasper:
        vauxmasper=cantper
        vsecmasper=vsecto
    
    print('las personas son', cantper)
    print('la cantidad de mujeres',cantm)
    print('el sueldo total',acumsueld)
    print('el secotr es',vsecto)

print('el sector ',vsecmasper,'es el que mas tiene con ',vauxmasper)

varchivo.close()