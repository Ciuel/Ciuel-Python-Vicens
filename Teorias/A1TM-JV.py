vacunados_COVID = {
    'Covishield': [1234567, 9874561, 5632147],
    'Spunik': [3214567, 4563217, 5698743, 9654872],
    'Sinopharm': [4563287]
}


def lista_vacunados(vacunados):
    try:
        vacuna = input('Ingrese: Covishield, Spunik o Sinopharm   ')
        print(vacunados[vacuna])
    except KeyError:
        print("Ups parece que hubo un error con el nombre de la vacuna...")


#Gestión información vacunados Entidad XX
opcion = input("Querés saber datos de los vacunados?. S/N   ")
try:
    while opcion.upper() == 'S':
        lista_vacunados(vacunados_COVID)
        opcion = input("Querés saber datos de los vacunados?. S/N  ")
except:
    print('Se produjo un error cuando se pidió información de vacunas')
