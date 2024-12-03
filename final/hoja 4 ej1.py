#realizar procedimientos de colas con 10 enteros y un programa
elementos=11
class tcola:
    frente=0
    final=0
    datos=[0]*elementos


def f_inicializar(pcola):
    pcola.frente=0
    pcola.final=0

def colavacia(pcola):
    if pcola.frente==pcola.final:
        vacia=True
    else:
        vacia=False
    return vacia

def colallena(pcola):
    vsiguiente=(pcola.final+1)%elementos
    if pcola.frente==vsiguiente:
        lleno=True
    else:
        lleno=False
    return lleno

def meter(pcola,pdato):
    if colallena==True:
        print('la cola esta llena')
    else:
        pcola.datos[pcola.final]=pdato
        pcola.final=(pcola.final+1)%elementos
    return pcola

def sacar(pcola):
    if colavacia==True:
        print('la cola esta vacia')
    else:
        print('se elimino ',pcola.datos[pcola.frente])
        pcola.frente=(pcola.frente+1)%elementos
    return pcola

cola=tcola

cargar=input('desea cragar?')

while cargar!='no':
    if colallena(cola)==True:
        print('la cola esta llena')
        cargar='no'
    else:
        dato=int(input('cargeu el numero'))
        meter(cola,dato)
        cargar=input('quiere cargar otro?')

eliminar=input('desea eliminar uno?')

while eliminar !='no':
    if colavacia(cola)==False:
        sacar(cola)
        eliminar=input('desea eliminar otro')
    else:
        print('la cola esta vacia')
        eliminar='no'

for c in range(cola.frente,cola.final):
    print(cola.datos[c])