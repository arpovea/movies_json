import json
from funciones import listarinformacion


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
		print (listarinformacion(doc))
	elif opcion==2:
		print()
	elif opcion==3:
		print()
	elif opcion==4:
		print()
	elif opcion==5:
		print()
	elif opcion==0:
		print("Hasta la proxima!")
		break;