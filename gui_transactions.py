import PySimpleGUI as sg
import gui_profile, utilities

def transaction_view():

    file_name = (utilities.get_current_user_str())

    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('Your transactions')],
        [sg.Output(size=(50,10), key='-OUTPUT-')],
        [sg.Cancel("Back")]
    ]
    window = sg.Window('SCAM-BANK™', layout)
    event, values = window.read()
    if event == 'Back':
        window.close()
        gui_profile.profile_page()



    window.close()