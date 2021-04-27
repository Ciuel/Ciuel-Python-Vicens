#Sea el siguiente código:
def incorporación(nombre, *args):
	lista = args + (nombre,)#Se agrega una coma para convertir nombre de un str a una tupla de un elemnto
	return lista
 
#Incorporación jugador en equipo
equipo = int(input('Indica en qué nro de equipo deseas incorporar un jugador: 1 o 2: '))
nombre = input ('Ingresa nombre del nuevo integrante: ')
if equipo == 1:
	nuevo = incorporación( nombre, 'Juan', 'Ana')
else:
	nuevo = incorporación( nombre, 'Pedro', 'Ernesto','Rosa','Elena')
 
print (f'El equipo {equipo} está conformado ahora por: {nuevo}')

'''Explicá por qué este código da error. Modificá el código de manera tal que permita solucionar el problema y que el programa realice lo que dice hacer.
b- Si la variable args recibiera a los parámetros variables en una lista, no hubiese dado error? Justifica la respuesta.
No, porque args itera los elementos que le llegan y los agrega a una tupla, ya que las tuplas son inmutables.'''
