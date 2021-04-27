import csv
import requests

with open("appstore_games.csv","r") as appg:
    reader=csv.reader(appg)
    maxlist=[]
    for row in reader:
      if "ES" in row[12].split(", ") and "0" == row[7]:
        print(row[2])
        try:
            maxlist.append((int(row[6]),row[4],row[2]))
        except ValueError:
            maxlist.append((0,row[4],row[2]))
    maxlist.sort(reverse=True)
    for e in range(0,10):
        print(maxlist[e][1])

        juego = maxlist[e][2]
        icon_url = maxlist[e][1]
        icono = requests.get(icon_url)
        try:
            with open(f'{juego}.jpg', 'wb') as f:
                f.write(icono.content)
        except FileNotFoundError:
            print(f"Nombre invalido: {juego}")



'''Pueden ir descargando el archivo con el que realizaremos la actividad de cualquiera de estas dos opciones :
https://archivos.linti.unlp.edu.ar/index.php/s/D0YR0jqOx1GQtSD
https://www.kaggle.com/tristan581/17k-apple-app-store-strategy-games?select=appstore_games.csv

Dado el dataset con datos de video juegos del Apple store.
Queremos:
 
(5 Python plus) listar los juegos gratuitos disponibles en idioma español.
(5 Python plus) los íconos (OPCIONAL en formato imagen, sino la url) de los 10 juegos con más calificaciones de usuarios (User Rating Count).
 
Compartir solución con @clauBanchoff y subir link a la tarea.
Opcional: pueden incluir manejo de excepciones donde consideren adecuado.
También pueden descargar el archivo en: https://archivos.linti.unlp.edu.ar/index.php/s/D0YR0jqOx1GQtSD


# Ayuda para el punto 2
import requests

juego = "Sudoku"
icon_url = "https://is2-ssl.mzstatic.com/image/thumb/Purple127/v4/7d/23/c6/7d23c660-aba8-308a-05c0-19385a377c0e/source/512x512bb.jpg"
icono = requests.get(icon_url)
with open(f'ejemplos/clase6/{juego}.jpg', 'wb') as f:
    f.write(icono.content)'''