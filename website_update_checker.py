from selenium import webdriver
import time
import requests
from PIL import Image

#Arguments:
telegram_bot_token = ""
website_link = ""
telegram_chat_id = ""
telegram_message = ""

with open(telegram_bot_token) as file:
    token = file.read()

driver = webdriver.Chrome('chromedriver')


driver.get(website_link)

while True:

    driver.save_screenshot("new_screenshot.png")

    
    driver.refresh()


    im1 = Image.open('default_screenshot.png')
    im2 = Image.open('new_screenshot.png')

    if list(im1.getdata()) == list(im2.getdata()):
        print("Identical")
        time.sleep(20)
    else:
        print("Different")
        params = {"chat_id":telegram_chat_id, "text":telegram_message}
        uurl = f"https://api.telegram.org/bot{token}/sendMessage"
        message = requests.post(uurl, params=params)

        #sleep 1000s
        time.sleep(1000)  
    
    
