from .TipoOrganismo import*

class ListaOrganismo():

    def __init__(self):
        self.Cabeza = None
        self.Cola = None
        self.Size = 0

    def InsertarLista(self, codigo, nombre):
        aux = Nodo(codigo, nombre)
        self.Size +=1
        if self.Cabeza == None:
            self.Cabeza = aux
            self.Cola = aux
        else:
            self.Cola.setNext(aux)
            self.Cola = aux

    def Imprimir(self):
        text = 'Las LIstas de Organismos guardados son:\n'
        if self.Cabeza == None:
            text = text + 'No hau Datos '
        aux = self.Cabeza
        while aux != None:
            text += str(aux.ImprimirTipo()+'\n')
            aux = aux.Next
        text += '|'

        return text    


y = ListaOrganismo()
y.InsertarLista('hola','juan')

y.InsertarCelda('12', '23', 'hola')
print(str(y.Imprimir()))       