#Moment05 kursolle inlämmningsuppgift - Arvid Anderson TE19D

#Imports
import PySimpleGUI as sg
import gui_login, register
from colorama import init
from colorama import Fore, Back, Style
init()

def register_form():
    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('Welcome, thank you for choosing SCAM-BANK™')],
        [sg.Text('Please enter your Name, Email, Address and Phone')],
        [sg.Text('First name', size=(15, 1)), sg.InputText()],
        [sg.Text('Last name', size=(15, 1)), sg.InputText()],
        [sg.Text('Email', size=(15, 1)), sg.InputText()],
        [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.Text('Phone', size=(15, 1)), sg.InputText()],
        [sg.Text('Address', size=(15, 1)), sg.InputText()],
        [sg.Submit("Register"), sg.Button("Back")]
    ]

    window = sg.Window('SCAM-BANK™', layout)
    event, values = window.read()

    if event == 'Register':
        fname = values[0]
        lname = values[1]
        email = values[2]
        password = values[3]
        phone = values[4]
        address = values[5]

        file_name = fname + "_" + lname + "_" + email + ".csv"

        if register.validate_user_file(file_name) == True:
            register.generate_user_file(file_name)
            register.add_user_content(file_name, fname, lname, email, password, phone, address)
            window.close()
            gui_login.login_form()
        else:
            sg.Popup("This user alredy exists, try using your credentials on the login form instead!")

    if event == 'Back':
        window.close()
        gui_login.login_form()

    window.close()