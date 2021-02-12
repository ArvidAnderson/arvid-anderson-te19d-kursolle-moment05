
import csv
import pathlib


def generate_user_file(file_name):
    with open(file_name, "w+"):
        pass

def add_user_content(file_name, fname, lname, email, password, phone, address):
    with open(file_name, "a") as f:
        file = csv.writer(f)
        file.writerow([fname, lname, email, password, phone, address])

def validate_user_file(file_name):
    file_name = pathlib.Path(file_name)
    if file_name.exists():
        print("This user is alredy registerd")
        return "abort"
    else:
        print("Can continue user is not registerd before")
        return "continue"



#Debug test
#generate_user_file("hej.csv")
#add_user_content("hej.csv", "Arvid Anderson", "arvid.anderson@outlook.com", "Dankster123", "073838383", "tsdawd")
#validate_user_file("hej.csv")