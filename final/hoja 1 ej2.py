#procedimientos con uno de tamano 10 y un programa
velementos=11
class Tcola:
    frente=0
    final=0
    dato=[0]*velementos

def fi_inicializar(pcola):
    pcola.frente=0
    pcola.final=0

def colavacia(pcola):
    if pcola.final==pcola.frente:
        vvacio=True
    else:
        vvacio=False
    return vvacio

def colallena(pcola):
    vsiguiente=(pcola.final+1)%velementos
    if vsiguiente==pcola.frente:
        vlleno=True
    else:
        vlleno=False
    return vlleno

def meter(pcola,pdato):
    if colallena(pcola)==True:
        print('la cola llena')
    else:
        pcola.dato[pcola.final]=pdato
        pcola.final=(pcola.final+1)%velementos
    return pcola

def sacar(pcola):
    if colavacia(pcola)==True:
        print('la cola etsa vacia')
    else:
        dato=pcola.dato[pcola.frente]
        pcola.frente=(pcola.frente+1)%velementos
        print('se elimino',dato)

#programa

cola=Tcola
fi_inicializar(cola)
cargar=input('desea cargar cositas')

while cargar!='no':
    vdato=int(input('cargue un numero'))
    meter(cola,vdato)
    cargar=input('caragr otro?')

eliminar=input('desea eliminar uno')

while eliminar!='no':
    sacar(cola)
    eliminar=input('eliminar otro')
for c in range(cola.frente,cola.final):
    print(cola.dato[c])