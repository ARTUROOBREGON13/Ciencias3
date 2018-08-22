from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*=/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol, lista):
    if arbol.valor == "+":
        return evaluar(arbol.izq, lista) + evaluar(arbol.der, lista)
    if arbol.valor == "-":
        return evaluar(arbol.izq, lista) - evaluar(arbol.der, lista)
    if arbol.valor == "/":
        return evaluar(arbol.izq, lista) / evaluar(arbol.der, lista)
    if arbol.valor == "*":
        return evaluar(arbol.izq, lista) * evaluar(arbol.der, lista)
    if arbol.valor == "=":
        x = evaluar(arbol.der, lista)
        y = evaluar(arbol.izq, lista)
        z = (x,y) 
        return z
    if arbol.valor.isalpha():
        x = buscar(lista, arbol.valor)
        if x != "":
            return x
        return arbol.valor
    return int(arbol.valor)

def buscar(lista, var):
    for item in lista:
        if item[0] == var:
            return item[1]
    return ""
    
pila = Pila()
lista = []
archivo = open("expresionesin.txt","r")
archivo2 = open("expresionesout.txt","w")

lineas = archivo.readlines()
for linea in lineas:
    if(len(linea)>1):
        linea = linea[:-1]
        pila = Pila()
        exp = linea.split(" ")
        convertir(exp,pila)
        valor = (evaluar(pila.desapilar(),lista))
        lista.append(valor)

for v in lista:
    archivo2.write(v[0] + " = " + str(v[1]) + "\n")
archivo.close()
archivo2.close()
