from instapy import InstaPy
gurun = str(input('Username to scrape followers from?: '))

from creds import username
from creds import password
session = InstaPy(username= str(username), password= str(password))
session.login()

print("===============================")
print("THIS IS GONNA TAKE A LONG TIME")
print("DO NOT TERMINATE THE TASK")
print("===============================")

session.grab_followers(username=str(gurun), amount="full", live_match=False, store_locally=True)
session.end()

print("=======================================================================================")
print("Go to the log file and replace quotation marks with apostrophes and get rid of spaces")
print("Then paste that into the followerlist.py file")
print("=======================================================================================")
