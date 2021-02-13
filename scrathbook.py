            amount_int = int(amount)
            if amount_int < balance:
                sg.popup(f"You are trying to withdraw more money then you currently have on your bankaccount, You have a total of ${balance}")
                window.close()
                withdraw_form()
            else:
                utilities.withdraw_balance(file_name, amount_int)
                window.close()
                gui_profile.profile_page()