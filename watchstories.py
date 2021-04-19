from instapy import InstaPy

storypercent = int(input("What percentage of stories to watch?: "))

import art

with open('creds.txt', 'r') as file:
    content = file.readlines()
    username = content[0]
    password = content[1]

session = InstaPy(username= str(username), password= str(password))
session.login()

from scraped import listt
session.set_do_story(enabled = True, percentage = int(storypercent), simulate = True)
session.story_by_users(listt)