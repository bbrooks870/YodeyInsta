import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 " "(KHTML, like Gecko) FxiOS/18.1 Mobile/16B92 Safari/605.1.15")
driver = webdriver.Firefox(profile)

cooldown = random.uniform(1, 2.5)
unfollowcooldown = random.uniform(900, 930)

import art

with open('creds.txt', 'r') as file:
    content = file.readlines()
    username = content[0]
    password = content[1]

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
driver.get('https://www.instagram.com/' + username)
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[3]/a/span').click()
time.sleep(1)
print('Starting to unfollow')

#while driver.find_elements_by_class_name('sqdOP.L3NKy._8A5w5'):
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

unfollowed = 0
while unfollowed <= 4:
    while driver.find_elements_by_class_name('sqdOP.L3NKy._8A5w5'): 
        scrollcounter = 0
        while scrollcounter <= 11:
            driver.find_element_by_class_name('sqdOP.L3NKy._8A5w5').click()
            time.sleep(0.5)
            driver.find_element_by_class_name('aOOlW.-Cab_').click()
            time.sleep(cooldown)
            scrollcounter = scrollcounter + 1
            print('Unfollowed the the ' + str(scrollcounter) + '. user')
        while scrollcounter == 12:
            time.sleep(0.5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            scrollcounter = scrollcounter - 12
            unfollowed = unfollowed + 1
            print('Scrolled for the ' + str(unfollowed) + '. time')
while unfollowed == 5:
    timeout = 0
    while timeout == 0:
        print("Chilling for a little bit so Instagram doesn't whoop your ass")
        time.sleep(float(unfollowcooldown))
        timeout = timeout + 1
    while timeout == 1:
        unfollowed = unfollowed - 3

driver.quit()
