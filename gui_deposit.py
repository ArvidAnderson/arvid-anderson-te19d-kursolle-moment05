
import PySimpleGUI as sg
import utilities
import gui_profile

def deposit_form():

    file_name = (utilities.get_current_user_str())

    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('DEPOSIT')],
        [sg.Text('Please enter your desierd amount to deposit!')],
        [sg.Text('Amount:', size=(15, 1)), sg.InputText()],
        [sg.Submit("Make deposit"),sg.Cancel("Back")]
    ]

    window = sg.Window('SCAM-BANK™', layout)
    event, values = window.read()
    if event == 'Make deposit':
        amount = values[0]
        try:
            amount_int = int(amount)
            utilities.deposit_balance(file_name, amount_int)
            window.close()
            gui_profile.profile_page()
        except:
            window.close()
            sg.popup("You can only deposit money (numbers) not text/words")
            deposit_form()
    if event == 'Back':
        window.close()
        gui_profile.profile_page()



    window.close()