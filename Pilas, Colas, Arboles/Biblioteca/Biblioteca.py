# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:24:00 2018
@author: TatianaVelandia
"""

class Cola:
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []



cola = Cola()

def mostrar(lista):
    print(" Tienes guardados los siguientes libros: ")
    for item in lista:
        print("* {}".format(item))
    print("")

def buscar(criterio, valor_busqueda):
    cola_resultados = Cola()
    for item in cola.items:
        if valor_busqueda == item[criterio]:
            cola_resultados.encolar(item)
    mostrar(cola_resultados.items)

def run():
    
    OPCIONES = "1) Ingresar un libro \n2) Busqueda de libros por género\n3) Busqueda de libros  por autor\n4) Busqueda de libros  por nombre\n5) Ver todos los libros"
    while True:
        opcion = int(input("Selecciona el número de la opción para la consulta: \n{}:\n".format(OPCIONES)))
        
        if opcion == 1:
            print("\tIngresar libro nuevo\n")
            nombre = input("Nombre del libro: ")
            autor = input("Autor del libro: ")
            genero = input("Género del libro: ")
            libro = {
                'Nombre': nombre,
                'Autor': autor,
                'Genero': genero
            }
            cola.encolar(libro)
            
        elif opcion == 2:
            print("\t Busca libros por género")
            gen_buscar = input("Ingresar búsqueda: ")
            buscar('Genero',gen_buscar)
            
        elif opcion == 3:
            print("\tBusca libros por autor")
            gen_buscar = input("Ingresar búsqueda: ")
            buscar('Autor',gen_buscar)

        elif opcion == 4:
            print("\tBusca libros por nombre")
            gen_buscar = input("Ingresar búsqueda: ")
            buscar('Nombre',gen_buscar)
        elif opcion == 5:
            mostrar(cola.items)
        else:
            print("Opcion no valida... ")
    
    
if __name__ == '__main__':
    run()
