import time
import random
from selenium import webdriver
gurun = str(input('Username to follow followers?: '))
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 " "(KHTML, like Gecko) FxiOS/18.1 Mobile/16B92 Safari/605.1.15")
driver = webdriver.Firefox(profile)

cooldown = random.uniform(2.5, 3.5)
unfollowcooldown = random.uniform(900, 930)

import art

with open('creds.txt', 'r') as file:
    content = file.readlines()
    username = content[0]
    password = content[1]

#driver.set_window_size(853, 853)
driver.set_window_size(480, 853)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]/button').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/section/div/button').click()
time.sleep(1)
print('Successfully logged in')
driver.get('https://www.instagram.com/' + gurun)
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a/span').click()
time.sleep(3)
print('Starting to follow')

#while driver.find_elements_by_class_name('sqdOP.L3NKy._8A5w5'):
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

follownu = 3
unfollowed = 0
while unfollowed <= 2:
    #while driver.find_element_by_class_name('sqdOP.L3NKy._8A5w5'):
    while driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/ul/div/li[' + str(follownu) + ']/div/div[2]/button'):
        scrollcounter = 0
        while scrollcounter <= 10:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/ul/div/li[' + str(follownu) + ']/div/div[2]/button').click()
            time.sleep(cooldown)
            follownu = follownu + 1
            scrollcounter = scrollcounter + 1
            #print('Followed the the ' + str(scrollcounter) + '. user')
        while scrollcounter == 11:
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            scrollcounter = scrollcounter - 11
            unfollowed = unfollowed + 1
            print('Scrolled for the ' + str(unfollowed) + '. time')
while unfollowed == 3:
    timeout = 0
    while timeout == 0:
        print("Chilling for a little bit so Instagram doesn't whoop your ass")
        time.sleep(float(unfollowcooldown))
        timeout = timeout + 1
    while timeout == 1:
        unfollowed = unfollowed - 3


print('Followed everyone')