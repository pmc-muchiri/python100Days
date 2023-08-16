from asyncio import sleep
from itertools import count
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from instabot import Bot


my_bot = Bot()

#login
my_bot.login(username="pmcmuchiri", password="Kijuyg3@4")

#followinhg
my_bot.follow("afronitaaa")


#follow multiple user
my_bot.follow_users(["missmumbe_faith","sheila_cansie","dorcasstephen20"])


#unfolllow the non followers
my_bot.unfollow_non_followers()

#Tips: Run this file once after 2 hours to avoid being bunned


""" uploading an immage """
#my_bot.upload_photo("image", caption="add python")


""" send messages to users """
#my_bot.send_message("your message", "designated account")

""" like a post """
#my_bot.like_user("account to like", amount=2)


""" commenting to a post """
#user_id = my_bot.get_username_from_user_id("accountid")
#media_id = my_bot.get_last_user_medias(user_id)
 
#my_bot.comment(media_id, "add your comment here")

""" get list of followes  """
""" followers_list = my_bot.get_user_followers("account")
following_list = my_bot.get_user_following("account")

for count, each_follower in enumerate(followers_list):
    if count <4:
        continue
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follower))
    

for count1, each_follow in enumerate(following_list):
     if count1 <4:
        continue
     sleep(5)
     print(my_bot.get_username_from_user_id(each_follow)) """


""" CHROME_DRIVER_PATH = "/home/pmc/development/chromedriver"
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
bot.follow() """