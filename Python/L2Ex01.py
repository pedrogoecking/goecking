#!-*- coding: utf8 -*-
lado_a = input("Lado A: ")
lado_b = input("Lado B: ")
lado_c = input("Lado C: ")
if lado_a < 1 or lado_b < 1 or lado_c < 1:
	print 'Não existe triângulo'
elif lado_a == lado_b == lado_c:
	print 'Equilátero'
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
	print 'Isósceles'
elif lado_a + lado_b >= lado_c and lado_a + lado_c >= lado_b and lado_b + lado_c >= lado_a and lado_a != lado_b != lado_c:
	print 'Escaleno'
else:
	print 'Não é triângulo'