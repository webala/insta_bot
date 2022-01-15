from selenium import webdriver
import os
import time


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('/usr/bin/chromedriver')

        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(5)
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys(self.username)
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

        #loginForm > div > div:nth-child(1) > div > label > input
        #self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        #//*[@id="loginForm"]/div/div[1]/div/label/input
        

    

if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')

    print(ig_bot.username)