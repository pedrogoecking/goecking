#author: Pedro Goecking
#!-*- coding: utf8 -*-
metros_quadrados = input("Área (m²): ")
def calculos(area):
	demanda_litros = area * 0.33
	demanda_latas = demanda_litros / 18
	if demanda_litros % 18 == 0:
		preco = demanda_latas * 80
		print 'Lata(s) de tinta necessária(s):',demanda_latas
	else:
		preco = (int(demanda_latas) + 1) * 80
		print 'Lata(s) de tinta necessária(s):', int(demanda_latas) + 1
	print 'Valor a pagar: R$', preco	
calculos(metros_quadrados)