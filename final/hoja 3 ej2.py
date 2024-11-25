#crear las funciones de pila y crear un programa de 10 elementos enteros

elemento=10

class Tpila:
    cima=0
    dato=[0]*elemento

def f_inicializar(ppila):
    ppila.cima=-1

def pilallena(ppila):
    if ppila.cima==elemento-1:
        llena=True
    else:
        llena=False
    return llena

def pilavacia(ppila):
    if ppila.cima==-1:
        vacia=True
    else:
        vacia=False
    return vacia

def meter(ppila,dato):
    if pilallena==True:
        print('la pila ya esta llena')
    else:
        ppila.cima+=1
        ppila.dato[ppila.cima]=dato
    return ppila

def sacar(ppila):
    if pilavacia==True:
        print('la pila esta vacia')
    else:
        print('se elimino', ppila.dato[ppila.cima])
        ppila.cima=ppila.cima-1
    return ppila

#programa

import random

pila=Tpila

f_inicializar(pila)

for c in range(0,elemento):
    if pilallena==True:
        print('la pila ya etsa cargada')
    else:
        dato=random.randint(0,100)
        print(dato)
        meter(pila,dato)

eliminar=input('desea eliminar uno?')

while eliminar!='no':
    if pilavacia==True:
        print('la pila ya esta vacia')
    else:
        sacar(pila)
        eliminar=input('eliminar otro?')

for c in range(0,pila.cima):
    print(pila.dato[c+1])