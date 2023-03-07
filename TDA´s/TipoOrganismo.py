class TipoOrganismo:

    def __init__(self, Codigo, Nombre):
        self.Codigo = Codigo
        self.Nombre = Nombre


class Nodo:
    def __init__(self, codigo, nombre):
        self.Next = None
        self.Tipo = TipoOrganismo(codigo, nombre)

    def  getNext (self):
            return self.Next
        

    def  assNext (self, Nodo):
        self.Next = Nodo          

    def getTipo (self):
        return self.Tipo
    
    def getNombreOrga(self):
         return self.Tipo.Nombre

    def getCodOrg (self):
         return self.Tipo.Codigo

    def ImprimirTipo(self):
         return 'Codigo del Organismo es', str(self.Tipo.Codigo),'Nombre del organismo es:', str(self.Tipo.Nombre)   