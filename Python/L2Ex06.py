#!-*- coding: utf8 -*-
salario_hora = input("Salário por hora (R$): ")
horas_mes = input("Horas trabalhadas no mês: ")
def calculos(salario, horas):
	salario_bruto = salario * horas
	desc_ir = salario_bruto * 0.11
	desc_inss = salario_bruto * 0.08
	desc_sindicato = salario_bruto * 0.05
	salario_liquido = salario_bruto - desc_sindicato - desc_inss - desc_ir
	print '-----------------------------'
	print 'Salário bruto: R$',salario_bruto
	print 'Desconto INSS: R$', desc_inss
	print 'Desconto sindicato: R$', desc_sindicato
	print 'Salário líquido: R$', salario_liquido

calculos(salario_hora, horas_mes)