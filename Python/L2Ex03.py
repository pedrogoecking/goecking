#author: Pedro Goecking
#!-*- coding: utf8 -*-
pesca = input("Pesca (kg): ")
if pesca > 50:
	excesso = pesca - 50
	multa = excesso * 4	
	print 'Excesso: ', excesso, '(kg) | Multa: R$', multa
else:
	excesso = 0
	multa = 0
	print 'Excesso: ', excesso, '(kg) | Multa: R$', multa