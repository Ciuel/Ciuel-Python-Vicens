import PySimpleGUI as sg
from ..Windows.menu import build
from ..Event_Handlers.menu import coursea_check,happy_check


def loop(menu_window):
    while True:
        event, values = menu_window.read()
        if event == sg.WIN_CLOSED:
            break
        coursea_check(event)
        happy_check(event)



def start():

    menu_window = build()
    loop(menu_window)

    menu_window.close()