from pathlib import Path
import csv
import utilities


def get_csv_files():
    csv_list = []
    paths = Path('./').glob('**/*.csv')
    for path in paths:
        path_in_str = str(path)
        csv_list.append(path_in_str)
    return csv_list

def check_login_details(email, password):
    csv_list = get_csv_files()
    for i in csv_list:
        with open(i, "r") as f:
            data = f.read()
            data_list = data.split(",")
            email_in_data = data_list[2]
            password_in_data = data_list[3]
            if email_in_data == email and password_in_data == password:
                utilities.set_current_user(i)
                return True


