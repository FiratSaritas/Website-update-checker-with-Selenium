from selenium import webdriver
import time
import requests
from PIL import Image

with open("token.txt") as file:
    token = file.read()

driver = webdriver.Chrome('chromedriver')

web_link = 'https://reserve-prime.apple.com/CH/de_CH/reserve/A/availability?iUP=N'

driver.get(web_link)

driver.save_screenshot("default_screenshot.png")

driver.quit()
    
    
