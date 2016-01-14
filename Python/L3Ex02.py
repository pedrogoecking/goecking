#author: Pedro Goecking
#!-*- coding: utf8 -*-
conta = input("Informe o valor: R$")
qtd_50 = int(conta) / 50
qtd_20 = (int(conta) - qtd_50 * 50) / 20
qtd_10 = ((int(conta) - qtd_50 * 50) - qtd_20 * 20) / 10
qtd_5 = (((int(conta) - qtd_50 * 50) - qtd_20 * 20) - qtd_10 * 10) / 5
qtd_2 = ((((int(conta) - qtd_50 * 50) - qtd_20 * 20) - qtd_10 * 10) - qtd_5 * 5) / 2
qtd_1 = (((((int(conta) - qtd_50 * 50) - qtd_20 * 20) - qtd_10 * 10) - qtd_5 * 5) - qtd_2 * 2)
print 'Cédulas de R$50,00:', qtd_50
print 'Cédulas de R$20,00:', qtd_20
print 'Cédulas de R$10,00:', qtd_10
print 'Cédulas de R$5,00:', qtd_5
print 'Cédulas de R$2,00:', qtd_2
print 'Cédulas de R$1,00:', qtd_1