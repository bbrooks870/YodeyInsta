from instapy import InstaPy

from creds import username
from creds import password
session = InstaPy(username= str(username), password= str(password))
session.login()
session.end()

print("=====================================")
print("NOW FOLLOW THE README.MD INSTRUCTIONS")
print("=====================================")

import scrapefollowers