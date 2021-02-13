# DÅLIGT STÄLLE FÖR VIKTIGT LISTA

import csv
import re

global current_user
current_user = []


# GETTERS
def generate_list(file_name):
    with open(file_name, "r") as f:
        csv_list = f.read()
        #csv_list = csv_list.split(",")
        csv_list = re.split(',|\n', csv_list) 
    return csv_list

def get_fname(file_name):
    csv_list = generate_list(file_name)
    fname = csv_list[0]
    return fname

def get_lname(file_name):
    csv_list = generate_list(file_name)
    lname = csv_list[1]
    return lname
    
def get_full_name(file_name):
    csv_list = generate_list(file_name)
    fullname = csv_list[0] + " " + csv_list[1]
    return fullname

def get_mail(file_name):
    csv_list = generate_list(file_name)
    mail = csv_list[2]
    return mail

def get_password(file_name):
    csv_list = generate_list(file_name)
    password = csv_list[3]
    return password

def get_phone(file_name):
    csv_list = generate_list(file_name)
    phone = csv_list[4]
    return phone

def get_address(file_name):
    csv_list = generate_list(file_name)
    address = csv_list[5]
    return address

def get_balance(file_name):
    csv_list = generate_list(file_name)
    balance = csv_list[6]
    return balance

def get_current_user():
    return current_user

def get_current_user_str():
    current_user_list = current_user
    str_creator = " "
    file_name = str_creator.join(current_user_list)
    return file_name

# SETTERS
def set_current_user(file_name):
    current_user.append(file_name)

def set_balance(file_name, amount):
    csv_list = generate_list(file_name)
    csv_list[6] = amount
    print(csv_list[6])
    csv
set_balance("user_user_user.csv", 1000)