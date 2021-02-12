
import PySimpleGUI as sg
import gui_register
import login
from colorama import init
from colorama import Fore, Back, Style
init()

def login_form():
    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('Welcome to SCAM-BANK™')],
        [sg.Text('Please enter your account details, email and password')],
        [sg.Text('Email', size=(15, 1)), sg.InputText()],
        [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.Submit("Login"),sg.Cancel("Exit"), sg.Button("No account? Register here")]
    ]

    window = sg.Window('SCAM-BANK™', layout)
    event, values = window.read()
    if event == 'Login':
        email = values[0]
        password = values[1]
        if login.check_login_details(email, password) == 'continue':
            pass
        else:
            sg.Popup("Login failed, please try again with the right credentials")
            login_form()


    if event == 'No account? Register here':
        window.close()
        gui_register.register_form()


    window.close()