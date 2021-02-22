
import csv
import pathlib


def generate_user_file(file_name):
    with open(file_name, "w+"):
        pass

def add_user_content(file_name, fname, lname, email, password, phone, address):
    with open(file_name, "a") as f:
        file = csv.writer(f)
        file.writerow([fname, lname, email, password, phone, address, "1000"])

def add_user_transactions(transactions_file):
    with open(transactions_file, "a") as f:
        file = csv.writer(f)

def validate_user_file(file_name):
    file_name = pathlib.Path(file_name)
    if file_name.exists():
        return False
    else:
        return True