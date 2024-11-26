#crear todas las funciones para trabajar sobre una pila y un programa que los use

velementos=10

class Tpilas:
    cima=0
    dato=[0]*velementos

def f_inicializar(ppila):
    ppila.cima=-1

def pilavacia(ppila):
    if ppila.cima==-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi

def pilallena(ppila):
    if ppila.cima==velementos-1:
        vauxi=True
    else:
        vauxi=False
    return vauxi

def meter(ppila,pdato):
    if pilallena(ppila)==False:
        ppila.cima+=1
        ppila.dato[ppila.cima]=pdato
    else:
        print('esta lleno')

def quitar(ppila):
    if pilavacia(ppila)==False:
        print('el elemento',ppila.dato[ppila.cima],'fue eliminado')
        ppila.cima=ppila.cima-1
    else:
        print('ya esta vacia')

#programa
pila=Tpilas

f_inicializar(pila)
cargardatos=input('desea cargar datos?')
while cargardatos!='no':
    dato=int(input('ingrese el numero'))
    if pilallena(pila)==False:
        meter(pila,dato)
        cargardatos=input('cargar otro?')
    else:
        print('la pila esta llena')
        cargardatos='no'

eliminardatos=input('desea eliminar un dato?')

while eliminardatos!='no':
    if pilavacia(pila)==False:
        quitar(pila)
        eliminardatos=input('eliminar otro')
    else:
        print('la pila etsa vacia')
        eliminardatos='no'

for c in range(0,pila.cima+1):
    print(pila.dato[c])