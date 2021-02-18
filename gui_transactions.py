import PySimpleGUI as sg
import gui_profile, utilities
import tkinter as TK

def transaction_view():

    file_name = utilities.get_current_user_str()
    transactions_name = utilities.get_transactions_name()

    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('Your transactions')],
        [sg.Output(size=(80, 20), key='_OUT_')],
        [sg.Cancel("Back")]
    ]

    window = sg.Window('SCAM-BANK™', layout, finalize=True)
    window.Element('_OUT_')._TKOut.output.bind("<Key>", lambda e: "break")
    with open(transactions_name, "r") as f:
        print(f.read())


    event, values = window.read()
    if event == 'Back':
        window.close()
        gui_profile.profile_page()
    


    window.close()