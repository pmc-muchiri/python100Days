from asyncio import sleep
from itertools import count
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from instabot import Bot


CHROME_DRIVER_PATH = "/home/pmc/development/chromedriver"
SIMILAR_ACCOUNT = "ulissesworld"
USERNAME = "pmcmuchiri"
PASSWORD = "Kijuyg3@4"

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()