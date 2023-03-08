class Organismo:

    def __init__(self, fila, columna, codigo):
        self.Fila = fila
        self.Columna = columna
        self.Codigo = codigo


class Node:

    def __init__(self, fila, columna, codigo):
        self.Next = None
        self.Org = Organismo(fila, columna, codigo)

    def getNext (self):
        return self.Next
    

    def setNext (self, Node):
        self.Next = Node

    def getOrganismo (self):
        return self.Org

    def getFila(self):
        return self.Org.Fila

    def getCols(self):
        return self.Org.Columna
    
    def getCod(self):
        return self.Org.Codigo
    
    def ImprimirOrg(self):
        return 'Codigo de Organismo: '+ str(self.Org.Codigo)+ ' En Coordenadas: ('+ str(self.Org.Fila) +',' + str(self.Org.Columna) + ')'
                


