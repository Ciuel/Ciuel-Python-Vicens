import PySimpleGUI as sg

WINDOW_FONT_SIZE = 15
WINDOW_FONT = "Helvetica"
BUTTON_SIZE = (25, 2)


def build():
    # yapf: disable

    layout = [[sg.Text(f"¿Que datos analizamos?",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2),text_color="purple")],
            [sg.Button('10 cursos de Coursea por rating', key="-COURSEA-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button('10 paises por ranking de generosidad', key="-HAPPY-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
    ]
    # yapf: enable
    
    return sg.Window("Menu",
                     layout,
                     finalize=True,
                     element_justification='center',
                     margins=(10, 10))
