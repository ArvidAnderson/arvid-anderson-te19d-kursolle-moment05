import PySimpleGUI as sg      
import gui

def profile_page():
    sg.theme('DarkTeal4')    # Keep things interesting for your users

    layout = [[sg.Text('SCAM-BANK™ LLC', size=(30, 1), font='Courier 20')],        
            [sg.Button('Deposit'), sg.Button('Withdraw'), sg.Button('Transactions'), sg.Button('Terminate Account'), sg.Exit()]]      

    window = sg.Window('SCAM-BANK™', layout)      

    while True:                             # The Event Loop
        event, values = window.read() 
        print(event, values)       
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      
        
        if event == 'Terminate Account':
            sg.popup("Are you sure you want to terminate your account?", button_type=1)
            #Add actions


    window.close()

profile_page()