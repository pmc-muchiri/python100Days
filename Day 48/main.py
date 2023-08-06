from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# path to your chromedriver
chrome_driver_path = "/home/pmc/development/chromedriver"

# create a service
service = Service(chrome_driver_path)

# pass the service to the webdriver.Chrome
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com/")
price = driver.find_element("price")
#price = driver.find_element_by_id("a-page")
print(price)

#driver.close()
driver.quit()
