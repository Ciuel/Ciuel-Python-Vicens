import PySimpleGUI as sg
import csv
import json
import os

def coursea_save(courses_list,output):
    """Se encarga de guardar la lista de cursos en un json

  Args:
      courses_list (list): Lista de cursos procesada
      output (json): Archivo de json para guardar los datos
  """
    json.dump(courses_list, output, indent=4)


def coursea_manipulation(info):
    """Procesa los datos segun el criterio, en este caso course_rating
    y devuelve una lista ordenada con los 10 mayores

  Args:
      info (csv): archivo csv con informacion de cursos

  Returns:
      [list]: lista procesada con la informacion a guardar
  """
    csvreader=csv.DictReader(info)
    courses_list=list(csvreader)
    courses_list.sort(key=lambda x: x["course_rating"], reverse=True)
    return list(map(lambda x: {"course_title": x["course_title"],"course_rating":x["course_rating"]}, courses_list[:10]))


def coursea_press():
    """Abre el csv o un popup en caso de no encontrarlo,
     crea o en caso de que ya exista abre el json y envía ambos a la funcion de procesamiento
     el archivo de coursea está bajo licencia GNU2 https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
  """
    try:
        output= open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}coursea_data.json"),"x")
    except FileExistsError:
        output= open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}coursea_data.json"),"w")
    try:
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}coursea_data.csv"),"r",encoding="utf-8") as info:
            coursea_save(coursea_manipulation(info),output)
    except FileNotFoundError:
        sg.popup_error("Archivo no encontrado", title="Archivo no encontrado")
    output.close()



def coursea_check(event):
    """Chequea si se presiono el boton de coursea y llama a la funcion de apertura de ser así

    Args:
        event (string): la key del evento actual
    """
    if event=="-COURSEA-":
        coursea_press()


def happy_save(happy_list, output):
    """Se encarga de guardar la lista de paises en un json

    Args:
        happy_list (list): Lista de paises procesada
        output (json): Archivo de json para guardar los datos
    """
    json.dump(happy_list, output, indent=4)


def happy_manipulation(info):
    """Procesa los datos segun el criterio, en este caso Generosity
        y devuelve una lista ordenada con los 10 mayores

    Args:
        info (csv): archivo csv con informacion de paises

    Returns:
        [list]: lista procesada con la informacion a guardar
    """
    csvreader = csv.DictReader(info)
    happy_list = list(csvreader)
    happy_list.sort(key=lambda x: x["Generosity"], reverse=True)
    return list(
        map(
            lambda x: {
                "Country or region": x["Country or region"],
                "Generosity": x["Generosity"]
            }, happy_list[:10]))


def happy_press():
    """Abre el csv o un popup en caso de no encontrarlo,
     crea o en caso de que ya exista abre el json y envía ambos a la funcion de procesamiento
     el archivo de World Happiness Report está bajo licencia Creative Commons Public Domain Dedication https://creativecommons.org/publicdomain/zero/1.0/
    """
    try:
        output= open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}happy_data.json"),"x")
    except FileExistsError:
        output= open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}happy_data.json"),"w")
    try:
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}happy_data.csv"),"r",encoding="utf-8") as info:
            happy_save(happy_manipulation(info), output)
    except FileNotFoundError:
        sg.popup_error("Archivo no encontrado", title="Archivo no encontrado")
    output.close()


def happy_check(event):
    """Chequea si se presiono el boton de happy y llama a la funcion de apertura de ser así

    Args:
        event (string): la key del evento actual
    """
    if event == "-HAPPY-":
        happy_press()
