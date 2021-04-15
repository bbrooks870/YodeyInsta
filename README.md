# YodeyInsta
This is one of my first Python projects. A simple InstaPy-based bot for Instagram marketing. Can follow from a list, scrape followers, watch stories and reels, and unfollow (not currently working due to a bug in InstaPy)
Preferably uses<a href="https://github.com/valentino1337/InstaPy">my fork of InstaPy</a>, but is complatible with the <a href="https://github.com/timgrossmann/InstaPy">vanilla one</a>

How to use:
1. Run the firstrun.py
2. After you've scraped enough followers, go to your Home directory/InstaPy/logs/your_username/relationship_data/target_username/followers/log file with date.json
3. Open it in nano or vim, because it can crash gedit and other GUI editors if you have thousands of followers scraped
4. Find and replace " with '
5. Find and replace spaces with nothing
6. Copy the whole file and paste it into followerlist.py file
7. Define it as the "tofollow" variable

Now you can run follow.py or watchstories.py

Dependencies:
<a href="https://github.com/valentino1337/InstaPy">InstaPy</a>
Firefox
Geckodriver
