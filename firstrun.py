import time
import sys

username = str(input('Your username?: '))
password = str(input('Your password?: '))

with open('creds.txt', 'w') as credentials:
    credentials.writelines(username + '\n')
    credentials.writelines(password)

print('============================================================')
print('Saved the credentials into the creds.txt file. Keep it safe!')
print('============================================================')
sys.exit()