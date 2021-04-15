from instapy import InstaPy
import random
cooldown = random.uniform(2, 3.5)

from creds import username
from creds import password
session = InstaPy(username= str(username), password= str(password))
session.login()

session.grab_following(username=username, amount="full", live_match=False , store_locally=False)
session.unfollow_users(amount="full", instapy_followed_enabled=False, allFollowing=True, style="LIFO", sleep_delay=float(cooldown))