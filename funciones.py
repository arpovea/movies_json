def listarinformacion (doc):
	lista=[]
	for i in doc:
		lista.append({'titulo':i['title'],'año':i['year'],'duracion':i['duration']})
	return lista

def contarinformacion (doc):
	lista=[]
	for i in doc:
		lista.append({'titulo':i['title'],'actores':len(i['actors'])})
	return lista

def palabrasdadas(palabra1,palabra2,doc):
	lista=[]
	for i in doc:
		if palabra1 in i['storyline'] and palabra2 in i['storyline']:
			lista.append({'titulo':i['title']})
	return lista

def actordado(actor,doc):
	lista=[]
	for i in doc:
		if actor in i['actors']:
			lista.append({'titulo':i['title']})
	return lista

def mediapuntuacionesurl(fecha1,fecha2,doc):
	lista=[]
	for i in doc:
		if int(i['year']) >= fecha1 and int(i['year']) <= fecha2 :
			lista.append({'titulo':i['title'],'puntuacion':round(sum(i['ratings'])/len(i['ratings']),2),'url':i['posterurl']})
	lista= sorted(lista, key=lambda k: k['puntuacion'])
	lista=lista[::-1]
	return lista
