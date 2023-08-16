import time
import tweepy
from selenium import webdriver

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/home/pmc/development/chromedriver"
TWITTER_API_KEY = "your_api_key"
TWITTER_API_SECRET = "your_api_secret"
TWITTER_ACCESS_TOKEN = "your_access_token"
TWITTER_ACCESS_SECRET = "your_access_secret"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()
        options.binary_location = "/path/to/chrome/binary"  # Specify Chrome binary location if needed
        options.add_argument("--headless")  # Run Chrome in headless mode if desired
        options.add_argument("--no-sandbox")  # May be necessary in some environments

        self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element_by_class_name("js-start-test")
        start_button.click()

        # Wait for the test to complete
        time.sleep(60)  # Adjust this time based on how long the test takes

        # Get the download and upload speed values
        self.down = self.driver.find_element_by_class_name("result-data-large.number.result-data-value.download-speed").text
        self.up = self.driver.find_element_by_class_name("result-data-large.number.result-data-value.upload-speed").text

        print(f"Download Speed: {self.down}")
        print(f"Upload Speed: {self.up}")

    def tweet_at_provider(self):
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth)

        tweet_text = f"Hey @YourProvider, my internet speed is {self.down} Mbps down and {self.up} Mbps up. Promised: {PROMISED_DOWN} Mbps down, {PROMISED_UP} Mbps up. #InternetSpeedTest"
        api.update_status(tweet_text)
        print("Tweet sent successfully!")

    def run(self):
        self.get_internet_speed()
        self.tweet_at_provider()
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.run()
