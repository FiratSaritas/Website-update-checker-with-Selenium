# Website-update-checker with Selenium

## About project
This repository covers a simple function, but one that makes life easier for some: It uses Selenium to visually check if the webpage has changed every 20 seconds (the [`time`](https://github.com/FiratSaritas/Website-update-checker-with-Selenium/blob/d2ebf43fbf380bd7d65831ab1225c9e5fb9b8255/website_update_checker.py#L33) can be adjusted in the code).
If there is a change in the webpage, it sends a message on telegram. This code can be used for many different websites, because it checks visually and no source code in the background.


## Getting Started

### Installation
Clone project locally
 ```sh
    git@github.com:FiratSaritas/Website-update-checker-with-Selenium.git
 ```

### Downloads

#### Chromedirver

You can download your matching Selenium Chromedriver here: https://chromedriver.chromium.org/downloads. and put the file in the same folder.


### Prerequisites 
Install required packages
 ```sh
    pip install -r requirements.txt
 ```

Set up Telegram bot with the [`BotFather`](https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq)


### Run project

First we want to make a screenshot of the default webpage as it looks at the moment and save it. Once you want to change the default screenshot, you just need to run this code again. To know which webpage to access, you need to add the link of the website in the [`code`](https://github.com/FiratSaritas/Website-update-checker-with-Selenium/blob/675b21fd356574d5ef6c66243645999781d5975c/default_image_creater.py#L11).

```sh
    python default_image_creater.py
 ```
Then we run the actual code that checks the page for changes by taking a new screenshot and comparing it to the default screenshot.
Here also arguments have to be added to the [`code`](https://github.com/FiratSaritas/Website-update-checker-with-Selenium/blob/de15df5395113a12b56b99ef0d6ae1bde61366a0/website_update_checker.py#L6). 
 
 ```sh
    python website_update_checker.py
 ```

