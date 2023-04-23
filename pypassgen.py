import generator
import PySimpleGUI as sg
import pyperclip

# prompt the user for the length of the password
length = int(sg.popup_get_text('Enter password length', 'Password Length'))

# prompt the user for the number of special characters
num_special_chars = int(sg.popup_get_text('Enter number of special characters', 'Special Characters'))

# prompt the user for the excluded characters
excl_chars = sg.popup_get_text('Enter the characters to be excluded', 'Excluded Characters')

# generate and print the password
password = generator.generate_password(length, num_special_chars, excl_chars)

# copy the password to the system clipboard
pyperclip.copy(password)

# show the generated password to the user in another popup
sg.popup('Your password is:' + password)

sg.popup_no_buttons("Generated password is copied to clipboard", title='PyPassGen', no_titlebar=True, auto_close=True,
                    modal=False)
