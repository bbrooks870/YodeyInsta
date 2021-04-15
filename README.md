# YodeyInsta
This is one of my first Python projects. A simple InstaPy-based bot for Instagram marketing. Can follow user followers (not working right now, fork if you can fix it), scrape followers, follow from the scraped list, watch stories and reels, and also unfollow if you happen to reach the following limit of 5000<br>
Uses <a href="https://github.com/valentino1337/InstaPy" target="_blank">my fork of InstaPy</a>, but is fully complatible with the <a href="https://github.com/timgrossmann/InstaPy">vanilla,</a> one

How to use:
1. Put your username and password into the variables in creds.py
2. If you want to watch stories and reels, you gotta scrape followers - that is the only function InstaPy is used for
3. To scrape followers, you should run firstrun.py (for the intial cookie creation) and it will then start scraping
4. If you need to follow user followers, just run the follow.py file
5. If you need to follow from a list you scraped, run the follow_from_a_list.py file
6. If you need to unfollow people, run the unfollow.py file
<br>
Dependencies:<br>
<a href="https://github.com/valentino1337/InstaPy">InstaPy</a><br>
Selenium<br>
Firefox<br>
Geckodriver
