# PyPassGen by m-sarabi

import generator
import PySimpleGUI as sg
import pyperclip

# dark look
sg.ChangeLookAndFeel('DarkBlack1')

# layout
# first row: password length, second row: special chars length, third row: excluded chars
# fourth row: checkbox force numbers, fifth row: generate button, and copy button, Sixth line: generated password

# making a group for the first three Input elements:
input_col = [
    [sg.Text('Password Length:', size=20), sg.Input(size=(5, 1), key='LENGTH', focus=True)],
    [sg.Text('Special Chars Count:', size=20), sg.Input(size=(5, 1), key='SPECIAL')],
    [sg.Text('Excluded Chars:', size=20), sg.Input(size=(5, 1), key='EXCLUDED')],
    [sg.Text('Force Numbers:', size=20), sg.Checkbox('', key='FORCE_NUMBERS')]
]

layout = [
    [sg.Column(input_col)],
    [sg.Button('Generate', key='GENERATE_BTN'), sg.Button('Copy', key='COPY_BTN', disabled=True)],
    [sg.Text('Your Password'), sg.Input(size=(40, 1), key='OUTPUT', use_readonly_for_disable=True, disabled=True)]
]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'GENERATE_BTN':
        # check if force numbers is enabled and all numbers are excluded:
        if values['FORCE_NUMBERS'] and all(c in values['EXCLUDED'] for c in '0123456789'):
            # open an error popup
            sg.popup_error("Can't generate  a password with all numbers excluded.")
            continue
        password = generator.generate_password(
            int(values['LENGTH']),
            int(values['SPECIAL']),
            values['EXCLUDED'],
            values['FORCE_NUMBERS']
        )
        window['OUTPUT'].update(disabled=False)
        window['OUTPUT'].Update(value=f'{password}')
        window['OUTPUT'].update(disabled=True),
        window['COPY_BTN'].update(disabled=False)

    if event == 'COPY_BTN':
        pyperclip.copy(window['OUTPUT'].Get())
window.close()
