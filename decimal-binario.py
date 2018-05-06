

def reversa(codigoObtenido):
	
	codigoBinario = ""

	longitud = len(codigoObtenido)

	posicion = longitud

	for x in codigoObtenido:

		codigoBinario += codigoObtenido[posicion-1]
		posicion -=1

	print(codigoBinario)


def convertir():

	#Declarcion de variables 
	divisor = 2
	cociente = 0
	residuo = 0

	#Variable para almacenar el codigoobtenido
	codigoObtenido = ""

	#Pedir por consola ,el numero  decimal a convertir
	dividendo = int(input(">>Digite numero decimal : "))

	#Bucle que se ejecutara mientras el cociente sea diferente de 1 y  termina cuando el cociente llega hacer igual 1
	while cociente != 1:

		#Vamos dividiendo entre divisor = 2
		cociente =  int(dividendo / divisor)

		#Obtenemos el residuo de cada division
		residuo = int(dividendo % divisor)

		#Vamos remplazando el valor del  del  divisor   con el cociente que vamos obteniendo
		dividendo = cociente

		#Vamos  concatenando los residuos que vamos obteniendo
		codigoObtenido += str(residuo)

	#
	codigoObtenido += str(cociente)
	
	reversa(codigoObtenido)


convertir()


