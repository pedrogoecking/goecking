#author: Pedro Goecking
#!-*- coding: utf8 -*-
cigarros = input("Cigarros/dia: ")
anos = input("Anos fumando: ")
print 'Dias a menos de vida:', float((cigarros * 365 * anos) * 10) / 60 / 24