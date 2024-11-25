#crear las funciones de pilas y  un programa que las use de 10 enteros
velemento=10
class tpila:
    cima=0
    vector=['']*velemento

def f_inicilizar(ppila):
    ppila.cima=-1

def pilallena(ppila):
    if ppila.cima==velemento-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi

def pilavacia(ppila):
    if ppila.cima==-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi

def meter(ppila,pdato):
    if pilallena(ppila)==False:
        ppila.cima+=1
        ppila.vector[ppila.cima]=pdato
    else:
        print('la pila esta llena')
    return ppila

def sacar(ppila):
    if pilavacia(ppila)==False:
        print('se elimino',ppila.vector[ppila.cima])
        ppila.cima-=1
    else:
        print('la pila esta vacia')
    return ppila

pila=tpila

f_inicilizar(pila)

cargar=input('desea cargar algo')

while cargar!='no':
    vdato=input('ingrese el dato')
    meter(pila,vdato)
    cargar=input('ingrese no para terminar')

eliminar=input('eliminar? ')
while eliminar!='no':
    sacar(pila)
    eliminar=input('eliminar otro')

for c in range(0,pila.cima):
    print(pila.vector[c+1])