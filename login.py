from pathlib import Path
import csv

def get_csv_files():
    csv_list = []
    paths = Path('./').glob('**/*.csv')
    for path in paths:
        path_in_str = str(path)
        csv_list.append(path_in_str)
    return csv_list

def check_login_details(email, password):
    csv_list = get_csv_files()
    for user_data in csv_list:
        with open(user_data, "r") as f:
            data = f.read()
            data = data.split(",")
            email_in_data = data[2]
            password_in_data = data[3]
            if email_in_data == email and password_in_data == password:
                return "continue"


