#misma mierda de colas

elementos=30
class Tcolas:
    frente=0
    final=0
    dato=[0]*elementos

def f_iniciliazar(pcola):
    pcola.frente=0
    pcola.final=0

def colavacia(pcola):
    if pcola.frente ==pcola.final:
        vacia=True
    else:
        vacia=False
    return vacia

def colallena(pcola):
    vsiguiente=(pcola.final+1)%elementos
    if vsiguiente==pcola.frente:
        llena=True
    else:
        llena=False
    return llena

def meter(pcola,pdato):
    if colallena(pcola)==True:
        print('la cola esta llena')
    else:
        pcola.dato[pcola.final]=pdato
        pcola.final=(pcola.final+1)%elementos
    return pcola

def sacar(pcola):
    if colavacia(pcola)==True:
        print('la cola esta vacia')
    else:
        print('se elimino ',pcola.dato[pcola.frente])
        pcola.frente=(pcola.frente+1)%elementos
    return pcola

cola=Tcolas

cargar=input('cargar datos ')

while cargar!='no':
    if colallena(cola)==True:
        print('la cola esta llena')
        cargar='no'
    else:
        vdato=int(input('dato'))
        meter(cola,vdato)
        cargar=input('otro')

eliminar=input('eliminar?')

while eliminar!='no':
    if colavacia(cola)==True:
        print('la cola esta llena')
        eliminar='no'
    else:
        sacar(cola)
        eliminar=input('sacar otro')

for c in range(cola.frente,cola.final):
    print(cola.dato[c])