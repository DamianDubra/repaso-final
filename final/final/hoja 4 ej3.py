#hacer una funcion que reciba una frase y devuelva la misma frase pero con mayuscula en cada palabra
#ejercicio de mierdaaaaaa
def mayusculizar(frase):
    frasenuev=frase.split(' ')
    for i in range(0,len(frasenuev)):
        palabra=frasenuev[i]
        if ord(palabra[0])>=97 and ord(palabra[0])<=122:
                asicx=ord(palabra[0])
                palabra=chr(asicx-32)+palabra[1:]
        for c in range(1,len(palabra)):
            if ord(palabra[c])>=65 and ord(palabra[c])<=90:
                papas=ord(palabra[c])
                palabra = palabra[:c] + chr(papas + 32) + palabra[c+1:]
        frasenuev[i]=palabra
    frase=' '.join(frasenuev)
    return frase

frase='HOLa comO esTAS'

frasenuev=mayusculizar(frase)

print(frasenuev)