# DÅLIGT STÄLLE FÖR VIKTIGT LISTA
current_user = []


# GETTERS
def generate_list(file_name):
    with open(file_name, "r") as f:
        csv_list = f.read()
        csv_list = csv_list.split(",")
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

def get_current_user():
    return current_user

# SETTERS
def set_current_user(file_name):
    current_user.append(file_name)