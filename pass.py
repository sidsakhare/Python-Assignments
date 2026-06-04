import os
from cryptography.fernet import Fernet

from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:/Users/ACER/Dropbox/PW skills Assignments/Python Projects/21 Python challanges/.env")

Master_pwd = os.getenv("Master_pwd")
print(Master_pwd)

master_pwd = input('what is the master password: ')
if master_pwd != Master_pwd:
    print("Wrong password. Access denied.")
    exit()


def write_key():  # defines a function to generate a key

    key = Fernet.generate_key()
    with open("key.key" , 'wb') as key_files: # .key a generic file extension used to store cryptographic keys in a persistent format
        key_files.write(key)

def load_key():  # defines a function to load a key
    with open("key.key" , 'rb') as read_key: # .key a generic file extension used to store cryptographic keys in a persistent format
        key = read_key.read()
        return key

key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as fa:
        for line in fa.readlines():
            #print(line.rstrip()) # strip() removes \n from code so 1 new line created after every view can be prevented
        
            data = line.rstrip()
            user, passw = data.split(' ,password is =')
            print('User:', user , ', Password :', fer.decrypt(passw.encode()).decode())


def add():

    name =input('Enter your name here: ')
    pwd = input('Enter yor password here: ')

    with open('password.txt', 'a') as fa :
        fa.write(name +' ,password is ='+ fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input("would you like to add a new password or view existing ones (add,view) or quit q=  ").lower()

    if mode == 'q':
        break
    elif mode == 'view':
        view()

    elif mode == 'add':
        add()
    
    else:
        print('invalid input')
        continue
