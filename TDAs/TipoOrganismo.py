from Organismo import*

class TipoOrganismo:

    
    def __init__ (self):
        self.Cabeza = None
        self.Cola = None
        self.Size = 0    

    def setUp(self, Codigo, Nombre):
        self.Codigo = Codigo
        self.Nombre = Nombre


    def InsertarCelda(self, fila, columna, codigo):
         aux1 = Node(fila, columna, codigo)
         if self.Codigo == codigo:
              if self.Cabeza == None:
                   self.Cabeza = aux1
                   self.Cola = aux1
                   self.Size += 1
              else:
                   self.Cola.setNext(aux1)
                   self.Cola = aux1       
                   self.Size += 1


class Nodo:
    def __init__(self, codigo, nombre):
        self.Next = None
        self.Tipo = TipoOrganismo(codigo, nombre)

    def  getNext (self):
            return self.Next
        

    def  setNext (self, Nodo):
        self.Next = Nodo          

    def getTipo (self):
        return self.Tipo
    
    def getNombreOrga(self):
         return self.Tipo.Nombre

    def getCodOrg (self):
         return self.Tipo.Codigo

    def ImprimirTipo(self):
         return 'Codigo del Organismo es: '+ str(self.Tipo.Codigo)+ ' Nombre del organismo es: '+ str(self.Tipo.Nombre)   
    

j = TipoOrganismo()
j.setUp('166', 'hola')
j.InsertarCelda('14','15','166')
