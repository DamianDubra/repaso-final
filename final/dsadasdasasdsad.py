#crear un programa que use las funciones de una cola con 50 elementos enteros
elementos=6
class Tcola:
    frente=0
    final=0
    datos=[0]*elementos

def f_inicializar(pcola):
    pcola.frente=0
    pcola.final=0

def colavacia(pcola):
    if pcola.frente==pcola.final:
        vacio=True
    else:
        vacio=False
    return vacio

def colallena(pcola):
    vsiguiente=(pcola.final+1)%elementos
    if vsiguiente== pcola.frente:
        lleno=True
    else:
        lleno=False
    return lleno

def meter(pcola,pdato):
    if colallena(pcola)==True:
        print('la cola esta llena')
    else:
        pcola.datos[pcola.final]=pdato
        pcola.final=(pcola.final+1)%elementos
    return pcola

def sacar(pcola):
    if colavacia(pcola)==True:
        print('la cola esta vacia')
    else:
        print('se elimino',pcola.datos[pcola.frente])
        pcola.frente=(pcola.frente+1)%elementos
    return pcola

cola=Tcola
f_inicializar(cola)

cargar=input('cargar uno')

while cargar!='no':
    vdato=int(input('numero'))
    meter(cola,vdato)
    cargar=input('otro')

eliminar=input('eliminar uno')

while eliminar!='no':
    sacar(cola)
    eliminar=input('otro')

for c in range (cola.frente,cola.final):
    print(cola.datos[c])

    

