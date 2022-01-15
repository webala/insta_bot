from selenium import webdriver
import os
import time


class InstagramBot:

    def __init__(self, username, password):
        """
        Inititalizes instance of InstagramBot class. Call login function

        Args:
            usename:str: Instagram username for user
            password:str: Instagram password for user

        
        Attributes:
            driver:Selenium.webdriver.Chrome: Chromedriver used to automate browser actions
        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')
        

        self.login()

    def login(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        self.driver.find_element_by_css_selector('input[name="username"]').send_keys(self.username)
        self.driver.find_element_by_css_selector('input[name="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        

    def nav_user(self, user):
        self.driver.get('{}{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)
        time.sleep(2)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
                                                         #//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button
                                                         #//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button
                                                         ##react-root > section > main > div > header > section > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div > span > span.vBF20._1OSdk > button
                                                         #//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button
        follow_button.click()

    

if __name__ == '__main__':
    ig_bot = InstagramBot('webdspam', 'morioanzenza')
    time.sleep(2)
    ig_bot.follow_user('_a.i.nun')