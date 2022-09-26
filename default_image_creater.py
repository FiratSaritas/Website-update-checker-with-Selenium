from selenium import webdriver
import time
import requests
from PIL import Image

with open("token.txt") as file:
    token = file.read()

driver = webdriver.Chrome('chromedriver')

web_link = ''

driver.get(web_link)

driver.save_screenshot("default_screenshot.png")

driver.quit()
    
    
