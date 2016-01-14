#author: Pedro Goecking
#!-*- coding: utf8 -*-
sal_antigo = input("Salário antigo: ")
perc_aumento = input("Aumento (%): ")
aumento = sal_antigo * float(perc_aumento) / 100
sal_atual = sal_antigo + aumento
print 'Salário atual de R$', sal_atual, 'Aumento de R$', aumento