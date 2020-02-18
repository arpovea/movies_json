import json
from funciones import listarinformacion
from funciones import contarinformacion
from funciones import palabrasdadas
from funciones import actordado
from funciones import mediapuntuacionesurl
with open("movies.json") as fichero:
	doc=json.load(fichero)

while True:
	print ('''
	Elige una opcion:
	1-Lista el título, año y duración de todas las películas.
	2-Muestra los títulos de las películas y el número de actores/actrices que tiene cada una.
	3-Muestra las películas que contengan en la sinopsis dos palabras dadas.
	4-Muestra las películas en las que ha trabajado un actor dado.
	5-Muestra el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.
	0-Para salir.
	''')
	opcion=int(input("Opcion: "))

	if opcion==1:
		for i in listarinformacion(doc):
			print('Año {} ---> Titulo: {} ---> Duracion: {}'.format(i['año'],i['titulo'],i['duracion']))
	elif opcion==2:
		for i in contarinformacion(doc):
			print('Titulo: {} ---> Nº Actores: {}'.format(i['titulo'],i['actores']))
	elif opcion==3:
		palabra1=str(input("Dime la primera palabra: "))
		palabra2=str(input("Dime la segunda palabra: "))
		print("Las peliculas que coinciden son: ")
		for i in palabrasdadas(palabra1,palabra2,doc):
			print('Titulo: {}'.format(i['titulo']))
	elif opcion==4:
		actor=str(input("Dime el actor: "))
		print("Las peliculas en las que trabaja son: ")
		for i in actordado(actor,doc):
			print('Titulo: {}'.format(i['titulo']))
	elif opcion==5:
		fecha1=int(input('Dime el año mas bajo: '))
		fecha2=int(input('Dime el año mas alto: '))
		for i in mediapuntuacionesurl(fecha1,fecha2,doc)[0:3]:
			print('Titulo: {} ---> Puntuacion: {} ---> Poster: {}'.format(i['titulo'],i['puntuacion'],i['url']))
	elif opcion==0:
		print("Hasta la proxima!")
		break;
