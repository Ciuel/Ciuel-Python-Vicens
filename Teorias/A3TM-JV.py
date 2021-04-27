Sea el siguiente código:
y = 9
def prueba1():
	def prueba2():
    	y = y + 1
	y = 5
	prueba2()
prueba1()
print (y)
Explicá por qué este código da error. Proponé una solución que no sea pasar por parámetros a la variable, para que no haya error y que el valor impreso sea 10.
