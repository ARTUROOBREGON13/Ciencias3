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
os.remove("resultado.txt")
archivo2 = open("resultado.txt","w")
lineas = archivo.readline()
#for linea in lineas:
 #   pila = Pila()
  #  exp = linea.split(" ")
   # convertir(exp,pila)
    #archivo2.write(str(evaluar(pila.desapilar()))+"\n")
print(lineas)

##exp = raw_input("ingrese l expresion en posfija: ").split(" ")

##pila = Pila()

##convertir(exp, pila)

##print evaluar(pila.desapilar())
