#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# vim: set fileencoding=uft-8 :
import lecturaPython as lec
import json

arr = ["C:\campeon\yasuo.py", "C:\campeon/adc.py", "C:\campeon\campeon.py", "C:\campeon\main.py"]


def leerArchivos(pRutas):
	arrJson =[]
	for n in range(0, len(arr)):
		archivo = open(pRutas[n])
		contenido = archivo.read()
		lec.setCodigo(contenido)
		arrJson += lec.obtenerJson()
	return json.dumps(arrJson)

print leerArchivos(arr)


