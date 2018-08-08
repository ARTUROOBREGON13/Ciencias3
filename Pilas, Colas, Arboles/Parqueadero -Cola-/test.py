# -*- coding: cp1252 -*-
def anadir(cola):
    codigo = raw_input('ingrese el codigo de la persona')
    nombre = raw_input('ingrese el nombre de la persona')
    placa = raw_input('ingrese la placa del vehiculo')
    cola.encolar(Persona(codigo, nombre, placa))
# -*- coding: utf-8 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]
        self.limiteEspacios = 30        

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        if self.limiteEspacios > 1:
            self.items.append(x)
            self.limiteEspacios-=1
            print('Espacios disponibles = '+ str(self.limiteEspacios))
        else :
            raise ValueError("El Parqueadero esta lleno")

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            if self.limiteEspacios<30:
                self.limiteEspacios+=1
                print('Sale '+self.items[0].getNombre()+', quedan '+str(self.limiteEspacios)+' espacios')
            return self.items.pop(0)
        except IndexError:
            raise ValueError("El parqueadero esta vacio")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def mostrar(self):
        for Persona in self.items:
            print(Persona.mostrarDatos()+'\n')

class Persona:
    """ Representa el contenedor de los datos: CodEst, Nombre y placa
    vehiculo"""

    def __init__(self,x ,y ,z):
        """ Inicializador de persona """
        self.CodEst = x
        self.Nombre = y
        self.Placa  = z

    def getNombre(self):
        return self.Nombre

    def getCodigo(self):
        return self.CodEst

    def getPlaca(self):
        return self.Placa

    def mostrarDatos(self):
        return self.getCodigo() +' '+ self.getNombre() +' '+ self.getPlaca()
    
p1 = Persona('20141020009', 'Arturo Buenaonda', 'BMX359')
p2 = Persona('20102035359', 'persona 2', 'BMX789')
p3 = Persona('20102035359', 'persona 3', 'BMW749')
p4 = Persona('20102035359', 'persona 4', 'ECM721')
p5 = Persona('20102035359', 'persona 5', 'ACM019')
p6 = Persona('20102035359', 'persona 6', 'IBM007')

p = Cola()
p.es_vacia()
p.encolar(p1)
p.encolar(p5)
p.encolar(p3)
p.encolar(p4)
p.encolar(p2)
p.encolar(p6)
p.es_vacia()
p.mostrar()
p.desencolar()

