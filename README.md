# YodeyInsta
This is one of my first Python projects. A simple InstaPy-based bot for Instagram marketing. Can follow user followers (not working right now, fork if you can fix it), scrape followers, follow from the scraped list, watch stories and reels, and also unfollow if you happen to reach the following limit of 5000<br>
Uses <a href="https://github.com/valentino1337/InstaPy" target="_blank">my fork of InstaPy</a>, but is fully complatible with the <a href="https://github.com/timgrossmann/InstaPy">vanilla</a> one

How to use:
1. Put your username and password into the variables in creds.py
2. If you want to watch stories and reels, you gotta scrape followers - that is the only function InstaPy is used for
3. To scrape followers, you should run firstrun.py (for the intial cookie creation) and it will then start scraping
4. If you need to follow user followers, <strike>just run the follow.py file</strike> scrape their followers
5. If you need to follow from a list you scraped, run the follow_from_a_list.py file
6. If you need to unfollow people, run the unfollow.py file
<br>
How to scrape:<br>
1. Scrape their followers using the scrapefollowers.py
2. After you've scraped enough followers, go to your Home directory/InstaPy/logs/your_username/relationship_data/target_username/followers/log file with date.json
3. Open it in nano or vim, because it can crash gedit and other GUI editors if you have thousands of followers scraped
4. Find and replace " with '
5. Find and replace spaces with nothing
6. Copy the whole file and paste it into followerlist.py file
7. Define it as the "tofollow" variable<br>
Dependencies:<br>
<a href="https://github.com/valentino1337/InstaPy">InstaPy</a><br>
Selenium<br>
Firefox<br>
Geckodriver
