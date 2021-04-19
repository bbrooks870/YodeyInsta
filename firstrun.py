from instapy import InstaPy
import time
import sys
import art

username = str(input('Your username?: '))
password = str(input('Your password?: '))

with open('creds.txt', 'w') as credentials:
    credentials.writelines(username + '\n')
    credentials.writelines(password)

print('============================================================')
print('Saved the credentials into the creds.txt file. Keep it safe!')
print('============================================================')

session = InstaPy(username= str(username), password= str(password))
session.login()

sys.exit()