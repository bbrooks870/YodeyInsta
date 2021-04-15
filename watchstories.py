from instapy import InstaPy

storypercent = int(input("What percentage of stories to watch?: "))

from creds import username
from creds import password
session = InstaPy(username= str(username), password= str(password))
session.login()

from followerlist import tofollow
session.set_do_story(enabled = True, percentage = int(storypercent), simulate = True)
session.story_by_users(tofollow)