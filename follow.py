from instapy import InstaPy
import random
cooldown = random.uniform(2, 3.5)

from creds import username
from creds import password
session = InstaPy(username= str(username), password= str(password))
session.login()
session.set_skip_users(skip_private=False)

print("===========================")
print("DO NOT TERMINATE THE TASK")
print("===========================")

from followerlist import tofollow
session.follow_by_list(tofollow, times=1, sleep_delay=float(cooldown), interact=False)

session.end()