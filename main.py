from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# URLs to be screenshot
urls = ['https://www.amazon.com', 'https://www.bestbuy.com', 'https://www.apple.com']

# folder to save screenshots
folder_name = "screenshots"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# set up the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")


# function to take screenshot of a URL
def take_screenshot(url, filename):
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)

    # get the height of the page
    height = driver.execute_script("return document.body.scrollHeight")

    # scroll down the page
    for i in range(height // 1000 + 1):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
    driver.set_window_size(1920, height)
    # save the screenshot
    driver.save_screenshot(f"{folder_name}/{filename}.png")
    driver.quit()


# take screenshot of each URL
for url, filename in zip(urls, range(len(urls))):
    take_screenshot(url, filename)
