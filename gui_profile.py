import PySimpleGUI as sg      
import gui
import gui_deposit
import gui_withdraw
import utilities



def profile_page():

    file_name = (utilities.get_current_user_str())
    fname = utilities.get_fname(file_name)
    balance = utilities.get_balance(file_name)

    sg.theme('DarkTeal4')

    layout = [[sg.Text('SCAM-BANK™ LLC', size=(30, 1), font='Helvetica 20')],
            [sg.Text(f"Welcome {fname}, thanks for choosing us!", font='Helvetica 12')],
            [sg.Text(f"Balance: ${balance}")],       
            [sg.Button('Deposit'), sg.Button('Withdraw'), sg.Button('Transactions'), sg.Button('Terminate Account'), sg.Exit()]]      

    window = sg.Window('SCAM-BANK™', layout)      

    while True:                             # The Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      
        if event == 'Deposit':
            window.close()
            gui_deposit.deposit_form()
        if event == 'Withdraw':
            window.close()
            gui_withdraw.withdraw_form()
        if event == 'Terminate Account':
            sg.popup("Are you sure you want to terminate your account?", button_type=1)
            #Add actions


    window.close()
