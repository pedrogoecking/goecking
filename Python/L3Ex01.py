#author: Pedro Goecking
#!-*- coding: utf8 -*-
num = input("Informe o número: ")
x, y, z = 1, 2 , 3
def triangulo(a, b, c, n):	
	if a * b * c == num:
		print n, 'é triangular e os multiplicandos são',a,',', b,'e',c
	elif a * b * c < n:
		a += 1
		b += 1
		c += 1
		triangulo(a, b, c, n)
	else:
		print n, 'não é triangular'
triangulo(x, y, z, num)