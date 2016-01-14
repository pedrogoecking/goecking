#author: Pedro Goecking
#!-*- coding: utf8 -*-
distancia = input("Distância (km): ")
velocidade_media = input("Velocidade média (km/h): ")
tempo_h = float(distancia) / velocidade_media
if tempo_h - int(tempo_h) > 0:
	tempo_m = (tempo_h - int(tempo_h)) * 60
	print 'Tempo aproximado de viagem:', int(tempo_h), 'horas e', int(tempo_m),'minutos'
else:
	print 'Tempo aproximado de viagem:', int(tempo_h), 'horas'