#un vector de tipo registro que etsa cargado y ordenado por legajo,, tiene legajo, apellidos, domicilio
#busqueda binaria por legajo

matriz=[[0]*30,
        ['']*30,
        ['']*30]

def busquedabin(matriz,elemento):
    vsenal=0
    vinicial=0
    vfinal=29
    posicion=-1
    while vsenal==0 and elemento<=matriz[0][vfinal] and elemento>=matriz[0][vinicial]:
        vcentral=(vinicial+vfinal)//2
        if elemento==matriz[0][vcentral]:
            posicion=vcentral
            vsenal=-1
        elif elemento>vcentral:
            vinicial=vcentral+1
        else:
            vfinal=vcentral-1
    if posicion<0:
        vsenal=-1
    return posicion

import random

for c in range(0,30):
    matriz[0][c]=c

print(matriz)

buscar=int(input('numero a buscara'))

posicion=busquedabin(matriz,buscar)

print(posicion)