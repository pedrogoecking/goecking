#author: Pedro Goecking
#!-*- coding: utf8 -*-
num_entrada = input("Número:")

pesquisa_primo = 2
a = 1
def prox_primo(a, n):
		if a < n:
			if n % a == 0:
				#Não número primo
				n+=1
				a=2
				prox_primo(a,n)
			else:
				a+=1
				primo(a, n)			
		else:
			#Número primo
			decompor(num_entrada, n)

prox_primo(a, pesquisa_primo)

def decompor(val_decompor, num_primo):
	num_entrada
	#desenvolver decomposição e armazenamento do primo