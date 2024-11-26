# funciones de pilar denuevo pero con 50 enteros

elementos=50

class Tpila:
    cima=0
    datos=[0]*50

def f_inicializar(ppila):
    ppila.cima=-1

def pilallena(ppila):
    if ppila.cima==elementos:
        lleno=True
    else:
        lleno=False
    return lleno

def pilavacia(ppila):
    if ppila.cima==-1:
        vacia=True
    else:
        vacia=False
    return vacia

def meter(ppila,pdato):
    if pilallena==True:
        print('la pila esta llena ')
    else:
        ppila.cima+=1
        ppila.datos[ppila.cima]=pdato
    return ppila

def sacar(ppila):
    if pilavacia==True:
        print('la pila esta vacia ')
    else:
        print('se elimno ',ppila.datos[ppila.cima])
        ppila.cima=ppila.cima-1
    return ppila

#progama
pila=Tpila

f_inicializar(pila)
carga=input('cargar datos')

while carga!='no':
    if pilallena(pila)==True:
        carga='no'
    else:
        vdato=int(input('cargue su dato '))
        meter(pila,vdato)
        carga=input('cargar otro ')

eliminar=input('eliminar ')

while eliminar!='no':
    if pilavacia==True:
        eliminar='no'
    else:
        sacar(pila)
        eliminar=input('eleiminar otro')

for c in range(0,pila.cima+1):
    print(pila.datos[c])