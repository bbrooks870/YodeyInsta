# YodeyInsta
This is one of my first Python projects. A simple Selenium-based, semi-InstaPy-based bot for Instagram marketing. Can follow user followers, scrape followers, follow from the scraped list, watch stories and reels, and also unfollow if you happen to reach the following limit of 7500<br>
Uses <a href="https://github.com/valentino1337/InstaPy" target="_blank">my fork of InstaPy</a>, but is fully complatible with the <a href="https://github.com/timgrossmann/InstaPy">vanilla</a> one

# How to use:
1. Run firstrun.py to save your credentials
2. If you want to watch stories and reels, you gotta scrape followers - that is the only function InstaPy is used for
3. To scrape followers, just run scrapefollowers.py
4. If you need to follow user followers, just run the follow.py file <strike>scrape their followers</strike>
5. If you need to follow from a list you scraped, run the follow_from_a_list.py file
6. If you need to unfollow people, run the unfollow.py file
# How to scrape:
1. Scrape followers using scrapefollowers.py
2. Go to Home directory/InstaPy/logs/your_username/relationship_data/target_username/followers/log file with date.json
3. Open it in nano or vim, GUI editors tend to crash if you have thousands of names there
4. Replace " with '
5. Replace spaces with nothing
6. Copy everything and paste it into the scraped.py list as the variable
# Dependencies:
<a href="https://github.com/valentino1337/InstaPy">InstaPy</a><br>
<a href="https://selenium.dev/">Selenium</a><br>
<a href="https://www.mozilla.org/en-US/firefox/new/">Firefox</a><br>
<a href="https://github.com/mozilla/geckodriver/releases">Geckodriver</a>
