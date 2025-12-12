import re
def email_sender(email):
    email_reg = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email_match = re.match(email,email_reg)
    if email_match:
        pass