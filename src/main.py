# Resolve the problem!!
import string, random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():

    random_len = random.randint(8,16)
    secure_password = ''
    secure_password += SYMBOLS[random.randint(0, 27)]
    secure_password += str(random.randint(0,9))
    #secure_password += 
    #secure_password += 
  
    print(secure_password)
    for element in range(0,random_len - 2):
        secure_password += string.ascii_letters[random.randint(0,46)]
    print(secure_password)
    return secure_password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
