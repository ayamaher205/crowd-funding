import datetime
from re import  fullmatch
def validate_name(input):
    pattern =r'[A-Za-z]{2,25}?'
    return fullmatch(pattern,input)


def validate_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(fullmatch(pattern,email)):
        return True
    return False

def validate_phone(phone):
    pattern = r'^01[0125][0-9]{8}$'
    return fullmatch(pattern,phone)

def validate_password(password):
    pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'
    return fullmatch(pattern,password)

def validate_date(date_text):
    try:
            datetime.date.fromisoformat(date_text)
    except ValueError:
            return False 

def validate_target(target):
    if not target.isnumeric():
        return False
