import PySimpleGUI as sg
from pathlib import Path
import gui_profile, utilities

def terminate_form():
    
    file_name = utilities.get_current_user_str()
    transactions_name = utilities.get_transactions_name()

    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('Are you sure you want to terminate your account? Actions are inreversible')],
        [sg.Button("yes"), sg.Button("Cancel")]
    ]
    window = sg.Window('Terminate account', layout, finalize=True)
    event, values = window.read()
    if event == 'Cancel':
        window.close()
        gui_profile.profile_page()
    if event == 'yes':
        window.close()
        file_path_transactions = Path(transactions_name)
        file_path_user = Path(file_name)
        sg.popup("Your account has now been terminated!")
        file_path_user.unlink()
        file_path_transactions.unlink()


    window.close()