# hacer todos los proceimientos de colas con 10 elemententos y un programa que los use
elementos=11
#lo podria poner con un imput
class Tcolas:
    frente=0
    final=0
    dato=[0]*elementos

def f_iniciliazarclass(pcola):
    pcola.frente=0
    pcola.final=0

def colallena(pcola):
    vsiguiente=(pcola.final+1)%elementos
    if pcola.frente==vsiguiente:
        lleno=True
    else:
        lleno=False
    return lleno

def colavacia(pcola):
    if pcola.frente==pcola.final:
        vacio=True
    else:
        vacio=False
    return vacio

def meter(pcola,Pdato):
    if colallena(pcola)==False:
        pcola.dato[pcola.final]=Pdato
        pcola.final=(pcola.final+1)%elementos
    else:
        print('la cola esta llena')
    return pcola

def sacar(pcola):
    if colavacia(pcola)==True:
        print('la cola ya esta vacia')
    else:
        print('se elimino',pcola.dato[pcola.frente])
        pcola.frente=(pcola.frente+1)%elementos
    return pcola

#programa
cola=Tcolas
colocar=input('desea agregar cosas')

while colocar!='no':
    if colallena(cola)==True:
        colocar='no'
        print('la cola esta llena')
    else:
        vdato=int(input('coloque el dato numerico'))
        meter(cola,vdato)
        colocar=input('otro? ')

elimnar=input('desea eliminar?')

while elimnar !='no':
    if colavacia(cola)==True:
        print('la cola esta vacia')
        elimnar='no'
    else:
        sacar(cola)
        elimnar=input('otro?')

for c in range(cola.frente,cola.final):
    print(cola.dato[c])