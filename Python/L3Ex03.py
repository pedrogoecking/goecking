#author: Pedro Goecking
#!-*- coding: utf8 -*-
num = input("Número:")
a = 2
def primo(a, n):
	if n > 0:
		if a < n:
			if n % a == 0:
				print n,'não é primo'
			else:
				a+=1
				primo(a, n)			
		else:
			print n,'é primo'
	else:
		print 'Entrada inválida'
primo(a, num)