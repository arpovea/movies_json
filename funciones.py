def listarinformacion (doc):
	lista=[]
	for elem in doc:
		año=elem.get("year")
		titulo=elem.get("title")
		duracion=elem.get("durations")
		lista.append(año)
		lista.append(titulo)
		lista.append(duracion)
	return lista