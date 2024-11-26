#la misma mierda de pilas
elementos=10
class Tpilas:
    cima=0
    datos=[0]*10

def f_inicializa(ppila):
    ppila.cima=-1

def pilallena(ppila):
    if ppila.cima==elementos:
        llean=True
    else:
        llean=False
    return llean

def pilavacia(ppila):
    if ppila.cima==-1:
        vacia=True
    else:
        vacia=False
    return vacia

def meter(ppila, pdato):
    if pilallena(ppila)==True:
        print('la ila esta llean')
    else:
        ppila.cima+=1
        ppila.datos[ppila.cima]=pdato
    return ppila

def sacar(ppila):
    if pilavacia(ppila)==True:
        print('la pila etsa vacia')
    else:
        print('se elimino',ppila.datos[ppila.cima])
        ppila.cima=ppila.cima-1
    return ppila

pila=Tpilas

cargar=input('cargara? ')

f_inicializa(pila)
while cargar!='no':
    if pilallena(pila)==True:
        print('la pila ya etsaba llena')
        cargar='no'
    else:
        vdato=int(input('dato: '))
        meter(pila,vdato)
        cargar=input('otro?')

eliminar=input('liminar uno')

while eliminar!='no':
    if pilavacia(pila)==True:
        print('la pila esta vacia')
        eliminar='no'
    else:
        sacar(pila)
        eliminar=input('eliminar otro')

for c in range (0,pila.cima+1):
    print(pila.datos[c])