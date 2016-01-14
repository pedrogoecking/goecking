#author: Pedro Goecking
#!-*- coding: utf8 -*-
val_mercadoria = input("Preço da mercadoria: ")
perc_desconto = input("Desconto (%): ")
desconto = val_mercadoria * float(perc_desconto) / 100
val_final = val_mercadoria - desconto
print 'Novo valor: R$', val_final, 'Desconto de R$', desconto