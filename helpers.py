import random
import string


def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'mail.com']
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

