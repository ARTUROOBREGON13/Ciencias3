from pila import *
from arbol import *
import os
lineas = []

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
            return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    
archivo = open("operaciones.txt","r")
archivo2 = open("resultado.txt","w")

lineas = archivo.readlines()
print(lineas)
for linea in lineas:
    if(len(linea)>1):
        linea = linea[:-1]
        pila = Pila()
        exp = linea.split(" ")
        print (exp)
        convertir(exp,pila)
        print(pila.items)
        valor = (evaluar(pila.desapilar()))
        archivo2.write(str(valor) + "\n")
        print(valor)
        

##exp = raw_input("ingrese l expresion en posfija: ").split(" ")

##pila = Pila()

archivo.close()
archivo2.close()

