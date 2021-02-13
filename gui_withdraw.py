
import PySimpleGUI as sg
import utilities
import gui_profile

def withdraw_form():
    file_name = (utilities.get_current_user_str())
    balance = utilities.get_balance(file_name)
    balance_int = int(balance)

    sg.theme('DarkTeal4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('WITHDRAW')],
        [sg.Text('Please enter your desierd amount to withdraw!')],
        [sg.Text('Amount:', size=(15, 1)), sg.InputText()],
        [sg.Submit("Make withdraw"),sg.Cancel("Back")]
    ]

    window = sg.Window('SCAM-BANK™', layout)
    event, values = window.read()
    if event == 'Make withdraw':
        amount = values[0]  
        try:
            amount_int = int(amount)
        except:
            sg.popup("You can only withdraw money (numbers) not text/words")
            window.close()
            withdraw_form()
        
        if amount_int < balance_int+1:
            utilities.withdraw_balance(file_name, amount_int)
            window.close()
            gui_profile.profile_page()
        else:
            sg.popup(f"You are trying to withdraw more money then you currently have on your bankaccount, You have a total of ${balance}")
            window.close()
            withdraw_form()
    if event == 'Back':
        window.close()
        gui_profile.profile_page()



    window.close()