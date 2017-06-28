#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# vim: set fileencoding=uft-8 :
import json
codigo = ""

def setCodigo(pCodigo):
    global codigo
    codigo = pCodigo

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
            listaAtributos.append(noaux2[listaPosAtributos[n]+5:(cadenaTMP.find("=")) + listaPosAtributos[n]-1])
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
        listaMetodos.append(cadenaTMP[cadenaTMP.find(":")+1:cadenaTMP.find("def")])
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
        cadenaTMP = codigoAPartirDeClase2[listaPosMetodos[n]+4 : len(codigoAPartirDeClase2)]
        #Se obteiene el codigo de la función desechando de la cadena temporal todo aquello que no sea eso
        #recorriendo desde el inicio de la función hasta encontral el siguiente "def"
        listaMetodos.append(cadenaTMP[cadenaTMP.find(":")+1:cadenaTMP.find("def")])
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
    return json.dumps(listaDiccionarios)

    
#print obtenerJson()

