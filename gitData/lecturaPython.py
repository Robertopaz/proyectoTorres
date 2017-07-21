#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# vim: set fileencoding=uft-8 :
import json
codigo = ""

def setCodigo(pCodigo):
    global codigo
    codigo = pCodigo+" 0"

def buscarNombresClases(pCodigo):
    listaClases = []
    listaPosClases = []
    pos_inicial = -1
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de
            # la última ocurrencia encontrada
            pos_inicial = codigo.index("class", pos_inicial+1)
            #Se recorre la posición hacia la siguiente de lo último encontrado
            listaPosClases.append(pos_inicial)
    except ValueError: # cuando ya no se encuentre class
        pos_inicial = -1
    for n in range(0, len(listaPosClases)):
        #Asignamos 100 caracteres más asumiento que el nombre de la clase medirá menos que eso
        cadenaTMP = codigo[listaPosClases[n] : listaPosClases[n]+100]
        #Obtenemos el nombre de la clase buscando hasta encontrar un punto apartir de de donde se encontró hasta ":"
        #Sumandole 6 posiciones que son las que ocupa "class " para si solo guardar el nombre
        listaClases.append(codigo[listaPosClases[n]+6:cadenaTMP.find(":")+listaPosClases[n]])
    return listaClases

def buscarMetodos(pClase):
    listaMetodos = []
    listaPosMetodos = []
    pos_inicial = -1
    #Eliminamos lo anterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase1 = codigo[codigo.index(pClase+":"):len(codigo)]
    #Eliminamos lo posterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase2 = codigoAPartirDeClase1[0: codigoAPartirDeClase1.find("class")]
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de la
            # la última ocurrencia encontrada a partir de la clase que recibimos como parametro
            #Se recorre la posición hacia la siguiente de lo último encontrado
            pos_inicial = codigoAPartirDeClase2.index("def", pos_inicial+1)
            listaPosMetodos.append(pos_inicial)
            if("class" in codigoAPartirDeClase2[pos_inicial:len(codigo)]):
                break
    except ValueError: # cuando ya no se encuentre self
        pos_inicial = -1
    for n in range(0, len(listaPosMetodos)):
        #Se obtiene una copia de la cadena en la posicion encontrada de n, hasta 50 caracteres más
        #asumiento que el nombre de la función no será más largo que eso
        cadenaTMP = codigoAPartirDeClase2[listaPosMetodos[n] : listaPosMetodos[n]+50]
        #Se obteiene nombre de la función desechando de la cadena temporal todo aquello que no sea eso
        listaMetodos.append(codigoAPartirDeClase2[listaPosMetodos[n]+4:(cadenaTMP.find(":")) + listaPosMetodos[n]])
    return listaMetodos

def buscarAtributos(pClase):
    listaAtributos = []
    listaPosAtributos = []
    pos_inicial = 1
    #Eliminamos lo anterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase1 = codigo[codigo.index(pClase+":"):len(codigo)]
    #Eliminamos lo posterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase2 = codigoAPartirDeClase1[0: codigoAPartirDeClase1.find("class")]
    if("__init__" in codigoAPartirDeClase2):
        #Eliminamos el contenido anterior al método "__init__" y también lo que hay fuera de el mismo
        #Para asegurarnos que solo se obtengan los atributos de la clase en su constructor
        noaux = codigoAPartirDeClase2[codigoAPartirDeClase2.find("__init__")+8:len(codigo)]
        noaux2 = noaux[noaux.find(":")+1: noaux.find("def")]
        try:
            while True:
                # cada vez buscamos desde un caracter más adelante de la
                # la última ocurrencia encontrada a partir de la clase que recibimos como parametro
                #Se recorre la posición hacia la siguiente de lo último encontrado
                pos_inicial = noaux2.index("self.", pos_inicial+1)
                listaPosAtributos.append(pos_inicial)
        except ValueError: # cuando ya no se encuentre def
            pos_inicial = -1
        for n in range(0, len(listaPosAtributos)):
            #Se obtiene una copia de la cadena en la posicion encontrada de n, hasta 50 caracteres más
            #asumiento que el nombre del atributo no será más largo que eso
            cadenaTMP = noaux2[listaPosAtributos[n] : listaPosAtributos[n]+50]
            #Se obtiene nombre del atributo desechando de la cadena temporal todo aquello que no sea eso
            listaAtributos.append(noaux2[listaPosAtributos[n]+5:(cadenaTMP.find("=")) + listaPosAtributos[n]])
    else:
        listaAtributos = []
    return listaAtributos

def buscarCodigos(pClase):
    listaMetodos = []
    listaPosMetodos = []
    pos_inicial = -1
    cadenaTMP = ""
    #Eliminamos lo anterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase1 = codigo[codigo.index(pClase+":"):len(codigo)]
    #Eliminamos lo posterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase2 = codigoAPartirDeClase1[0: codigoAPartirDeClase1.find("class")]
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de la
            # la última ocurrencia encontrada a partir de la clase que recibimos como parametro
            #Se recorre la posición hacia la siguiente de lo último encontrado
            pos_inicial = codigoAPartirDeClase2.index("def", pos_inicial+1)
            listaPosMetodos.append(pos_inicial)
    except ValueError: # cuando ya no se encuentre self
        pos_inicial = -1
    for n in range(0, len(listaPosMetodos)):
        #Se obtiene una copia de la cadena en la posicion encontrada de n+4 que es donde está el "def "
        #hasta la longitud del codigo cortado donde se encuentra un class, de tal forma que obtenemos
        #todo el contenido del codigo sin importar su longitud
        cadenaTMP = codigoAPartirDeClase2[listaPosMetodos[n]+4 : len(codigoAPartirDeClase2)]
        #Se obteiene el codigo de la función desechando de la cadena temporal todo aquello que no sea eso
        #recorriendo desde el inicio de la función hasta encontral el siguiente "def"
        listaMetodos.append(cadenaTMP[cadenaTMP.find(":")+1:cadenaTMP.find("def")].strip())
    return listaMetodos

def buscarCodigoMetodoUltimaClase(pClase):
    listaMetodos = []
    listaPosMetodos = []
    pos_inicial = -1
    cadenaTMP = ""
    #Eliminamos lo anterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase1 = codigo[codigo.index(pClase+":"):len(codigo)]
    #Eliminamos lo posterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase2 = codigoAPartirDeClase1[0: codigoAPartirDeClase1.find("\n\n")]
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de la
            # la última ocurrencia encontrada a partir de la clase que recibimos como parametro
            #Se recorre la posición hacia la siguiente de lo último encontrado
            pos_inicial = codigoAPartirDeClase2.index("def", pos_inicial+1)
            listaPosMetodos.append(pos_inicial)
    except ValueError: # cuando ya no se encuentre self
        pos_inicial = -1
    for n in range(0, len(listaPosMetodos)):
        #Se obtiene una copia de la cadena en la posicion encontrada de n+4 que es donde está el "def "
        #hasta la longitud del codigo cortado donde se encuentra un class, de tal forma que obtenemos
        #todo el contenido del codigo sin importar su longitud
        cadenaTMP = codigoAPartirDeClase2[listaPosMetodos[n]+4: len(codigoAPartirDeClase2)]
        #Se obteiene el codigo de la función desechando de la cadena temporal todo aquello que no sea eso
        #recorriendo desde el inicio de la función hasta encontral el siguiente "def"
        listaMetodos.append(cadenaTMP[cadenaTMP.find(":")+1:cadenaTMP.find("def")].strip())
    return listaMetodos


def buscarRelaciones(pClase):
    clasesRelacionadas = []
    listaClases = buscarNombresClases(codigo)
    #Eliminamos lo anterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase1 = codigo[codigo.index(pClase+":"):len(codigo)]
    #Eliminamos lo posterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeClase2 = codigoAPartirDeClase1[0: codigoAPartirDeClase1.find("class")]
    #Buscamos todas las instanciaciones de objetos dentro de la clase
    for n in range(0, len(listaClases)):
        #Buscamos si existe una instanciación con los elementos distintivos "= "+nombreClase+"("
        rel = codigoAPartirDeClase2.find("= "+listaClases[n]+"(")
        #Si el número es diferente a -1 es porque si se encontró relación, por lo tanto se agrega a la lista
        if(rel != -1):
            clasesRelacionadas.append(listaClases[n])
    return clasesRelacionadas

def buscarObjetosInstanciados(pClase):
    listaPosInstancias = []
    listaObjetos = []
    pos_inicial = -1
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de la
            # la última ocurrencia encontrada a partir de la clase que recibimos como parametro
            #Se recorre la posición hacia la siguiente de lo último encontrado
            pos_inicial = codigo.index(" = "+pClase+"(", pos_inicial+1)
            listaPosInstancias.append(pos_inicial)
    except ValueError: # cuando ya no se encuentre self
        pos_inicial = -1
    for n in range (0, len(listaPosInstancias)):
        #print listaPosInstancias[n]
        aux = codigo[listaPosInstancias[n]-50:listaPosInstancias[n]]
        aux2 = aux[::-1]
        aux3 = aux2[0:aux2.find("\n")]
        aux4 = aux3[::-1]
        listaObjetos.append(aux4.strip())
        if(len(listaObjetos)==0):
            listaObjetos.append("Vacío")
    return listaObjetos

def obtenerJson():
    #Se obtienen las clases del codigo
    listaClases = buscarNombresClases(codigo)
    #Se crea una lista que contendra los diccionarios de las clases con su nombre,atributos y métodos
    listaDiccionarios = range(len(listaClases))
    for n in range(0,len(listaDiccionarios)):
        #Se declara la plantilla del dicciionario
        plantillaDiccionario= {}
        #Se asigna el nombre de la clase al atributo del diccionario del mismo nombre
        plantillaDiccionario['nombre'] = listaClases[n]
        #Se asignan los atributos de la clase al atributo del diccionario del mismo nombre
        plantillaDiccionario['atributos'] = buscarAtributos(listaClases[n])
        #Se asignan los métodos de la clase al atributo del diccionario del mismo nombre
        plantillaDiccionario['metodos'] = buscarMetodos(listaClases[n])
        #Se asignan los contenidos de los metodos de la clase al atributo del diccionario del mismo nombre
        if(n == len(listaDiccionarios)-1):
            plantillaDiccionario['contenidos'] = buscarCodigoMetodoUltimaClase(listaClases[n])
        else:
            plantillaDiccionario['contenidos'] = buscarCodigos(listaClases[n])
        #Se asignan las relaciones de las clases al atributo del diccionario del mismo nombre
        plantillaDiccionario['relaciones'] = buscarRelaciones(listaClases[n])
        #Se guarda el diccionario actual en la lista para no perderlo
        listaDiccionarios[n] = plantillaDiccionario
    #Se returna el json de la lista
    return listaDiccionarios

#Obtiene las llamadas de la pInstancias, en el pMetodo, comparando con pContenido
def obtenerLlamadas(pInstancia, pMetodo, pContenido):
    listaLlamadas = ""
    listaPosLlamada = []
    pos_inicial = -1
    try:
        while True:
            # cada vez buscamos desde un caracter más adelante de la
            # la última ocurrencia encontrada a partir de la clase que recibimos como parametro
            #Se recorre la posición hacia la siguiente de lo último encontrado
            pos_inicial = pContenido.index(pInstancia+"."+pMetodo[0:pMetodo.find("(")], pos_inicial+1)
            listaPosLlamada.append(pos_inicial)
    except ValueError: # cuando ya no se encuentre self
        pos_inicial = -1
    for n in range(0, len(listaPosLlamada)):
        #Se obtiene una copia de la cadena en la posicion encontrada de n, hasta 50 caracteres más
        #asumiento que el nombre de la función no será más largo que eso
        cadenaTMP = pContenido[listaPosLlamada[n] : listaPosLlamada[n]+50]
        #Se obteiene nombre de la función desechando de la cadena temporal todo aquello que no sea eso
        #Se le concatena un coma para después poder separarlos en arreglos por un split de comas
        listaLlamadas += pContenido[listaPosLlamada[n]:(cadenaTMP.find("(")) + listaPosLlamada[n]]+","
        #Antes de regresarlo se elimina la última coma para evitar crear un elemento vacío en el arreglo que se haga después por split
    return listaLlamadas[0:len(listaLlamadas)-1]

#Funcion para buscar el contenido de un método individualmente
#Mientras no se el último método de la última clase funcionará
def buscarCodigoPorMetodo(pMetodo):
    contenidoMetodo = ""
    listaPosMetodos = []
    pos_inicial = -1
    cadenaTMP = ""
    #Eliminamos lo anterior al método de la cual vamos a obtener los métodos
    codigoAPartirDeMetodo1 = codigo[codigo.find("def "+pMetodo+":"):len(codigo)]
    #Eliminamos lo posterior al método de la cual vamos a obtener los métodos
    codigoAPartirDeMetodo2 = codigoAPartirDeMetodo1[0: codigoAPartirDeMetodo1.find("class")]
    return codigoAPartirDeMetodo2.strip()

#Función especial para poder obtener el contenido de un método individualmente
#Funcionará solo si se usa para buscar el último método de la última clase
def buscarCodigoPorMetodoUltimaClase(pMetodo):
    contenidoMetodo = ""
    listaPosMetodos = []
    pos_inicial = -1
    cadenaTMP = ""
    #Eliminamos lo anterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeMetodo1 = codigo[codigo.find("def "+pMetodo+":"):len(codigo)]
    #Eliminamos lo posterior a la clase de la cual vamos a obtener los métodos
    codigoAPartirDeMetodo2 = codigoAPartirDeMetodo1[codigoAPartirDeMetodo1.find(":")+1: codigoAPartirDeMetodo1.find("\n\n")]
    return codigoAPartirDeMetodo2.strip()

def obtenerJsonSecuencia(pMetodo):
    #Se crean una lista donde se almacenarán los objetos instanciados en pMetodo
    listaObjetosEnElMetodo = []
    #Se obtienen todas las clases para obtener todos sus métodos
    listaTodasLasClases = buscarNombresClases(codigo)
    #Se crea una variable que recibirá todos los métodos de todas las clases
    listaMetodosABuscar = []
    #Se crea un diccionario para poder acceder a las listas de las instancias de objetos según atributo
    listaInstanciasTodasLasClases = {}
    #Se obtienen todos los métodos de todo el archivo obteniendo las listas de métodos clase por clase
    for n in range(0, len(listaTodasLasClases)):
        listaMetodosABuscar+= buscarMetodos(listaTodasLasClases[n])
        listaInstanciasTodasLasClases["instancias"+listaTodasLasClases[n]] = buscarObjetosInstanciados(listaTodasLasClases[n])
    #Se declara una variable que contrendrá el código del método
    contenidos = ""
    #Se recorren los metodos existentes
    for n in range(0,len(listaMetodosABuscar)):
        #Si se encuentra un método que coincida con el metodo recibido en el parametro se entra a la condición
        if(listaMetodosABuscar[n] == pMetodo):
            #Si es el último método de la última clase se obtiene el contenido de ese método de forma dierente a los demás métodos
            if(n == len(listaMetodosABuscar)-1):
                contenidos = buscarCodigoPorMetodoUltimaClase(listaMetodosABuscar[n])
            #Sino es él último método del archivo se obtiene el contenido de ese método de forma similar a todos menos el último
            else:
                contenidos = buscarCodigoPorMetodo(listaMetodosABuscar[n])
    #Recorrermos todas las clases para obtener todos los atributos del diccionario que tienen su nombre
    for n in range(0, len(listaTodasLasClases)):
        #Recorremos todos los elementos de un atributo "instancias" + el elemento n de la lista de las clases
        for o in range(0, len(listaInstanciasTodasLasClases["instancias"+listaTodasLasClases[n]])):
            #Creamos una variable auxiliar y le asignamos el valor de la posición donde se encuentre el elemento del atributo en la posición o
            aux = contenidos.find(listaInstanciasTodasLasClases["instancias"+listaTodasLasClases[n]][o])
            #Si el valor de la variable auxiliar es diferente de uno quiere decir que se encontró en el contenido del método
            #Por lo que lo guardamos en la lista de objetos instanciados en el método
            if(aux != -1):
                listaObjetosEnElMetodo.append(listaInstanciasTodasLasClases["instancias"+listaTodasLasClases[n]][o]+":"+listaTodasLasClases[n])
    #Creamos un diccionario el cual regresaremos como el json de de ésta función
    diccionarioRegresar = {}
    #Creamos una variable de string la cual tendrá contenidas las llamadas obtenidas del método obtenerLLamadas            
    listaDiccionarios = ""
    #Se recorren los metodos existentes
    for o in range(0,len(listaObjetosEnElMetodo)):
        #Se obtiene solo el nombre del objeto instanciado
        pInstancia = listaObjetosEnElMetodo[o].split(":")
        #Se recorren todos los métodos de todo el archivo para buscar llamadas que coincidan con las instancias y métodos escritras
        for n in range(0,len(listaMetodosABuscar)):
                #Si la llamada del método con la listaObjetosEnElMetodo en la posición o no está vacía se agrega el contenido al string listaDiccionarios
                #Debido a que la función obtenerLlamadas() busca con todas las combinaciones de llamadas posibles de métodos y objetos
                #a veces regresa contenidos vacío, por eso que se verifique antes si tiene contenido o no
                if(obtenerLlamadas(pInstancia[0], listaMetodosABuscar[n], contenidos) != ""):
                    #Se le concatena una coma al final para poder separarlo luego en una lista con un split
                    listaDiccionarios += obtenerLlamadas(pInstancia[0], listaMetodosABuscar[n], contenidos)+","
    #Se asigna el contenido de la lista de objetos en el método al atributo objetos en el diccionarioRegresar
    diccionarioRegresar["objetos"] = listaObjetosEnElMetodo
    #Se le quita la última coma a lo que se obtuvo de la función de obtenerLlamadas() y se convierte en arreglo con un split
    llamadas = listaDiccionarios[0:len(listaDiccionarios)-1].split(",")
    #Se asigna el contenido de la lista de llamadas en el método al atributo llamadas en el diccionarioRegresar
    diccionarioRegresar["llamadas"] = llamadas
    diccionarioRegresar["contenidos"] = contenidos[contenidos.find("):")+2:len(contenidos)]
    return json.dumps(diccionarioRegresar)

    
#print obtenerJson()

