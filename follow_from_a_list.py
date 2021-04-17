from instapy import InstaPy
import random
cooldown = random.uniform(2, 3.5)

#from creds import username
#from creds import password

with open('creds.txt', 'r') as file:
    content = file.readlines()
    username = content[0]
    password = content[1]

session = InstaPy(username= str(username), password= str(password))
session.login()
session.set_skip_users(skip_private=False)

print("===========================")
print("DO NOT TERMINATE THE TASK")
print("===========================")

from scraped import listt
session.follow_by_list(listt, times=1, sleep_delay=float(cooldown), interact=False)

session.end()