from xml.dom import minidom
import xml.etree.ElementTree as ET



xmlMuestra = ET.Element('datosMarte')
#print('INGRESE LA RUTA ABSOLUTA DEL DOCUMENTO A INSEPECCIONAR')
#ruta = input()
arch = minidom.parse('IPC2_Proyecto1_201807185\EntradaEjemplo.xml')
listaOrg = arch.getElementsByTagName('listaOrganismos')
print('Lista de organismos')
for Org in listaOrg:
    lorganismo = Org.getElementsByTagName("organismo")
    for x in lorganismo:
        code = x.getElementsByTagName('codigo')[0]
        name = x.getElementsByTagName('nombre')[0]
        print('Codigo de la Muestra',code.firstChild.data,'Nombre de la muestra:', name.firstChild.data)

# Lista de Muestras
listMu = arch.getElementsByTagName('listadoMuestras')
print ('Listado de Muestras')
for y in listMu:
    muestra = y.getElementsByTagName('muestra')
    for z in muestra:
        code = z.getElementsByTagName('codigo')[0]
        desc = z.getElementsByTagName('descripcion')[0]
        fila = z.getElementsByTagName('filas')[0]
        columna = z.getElementsByTagName('columnas')[0]
        print('Codigo Muestra', code.firstChild.data, 'descripcion Muestra', desc.firstChild.data,
              'Numero Filas', fila.firstChild.data,'Numero Columna', columna.firstChild.data)
        print()
        listCelViv = z.getElementsByTagName('listadoCeldasVivas')
        for i in listCelViv:
            celdaViva = i.getElementsByTagName('celdaViva')
            for j in celdaViva:
                filaO = j.getElementsByTagName('fila')[0]
                columnaO = j.getElementsByTagName('columna')[0]
                codeOrg = j.getElementsByTagName('codigoOrganismo')[0]
                print('Celda Viva en:', filaO.firstChild.data, columnaO.firstChild.data, 'Codigo Organismo:', codeOrg.firstChild.data)
    print()

