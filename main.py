from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from PIL import Image
from selenium.webdriver.chrome.options import Options

print("the script is running")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# opening the url fullscreen in chrome, having the proper chrome driver is important
s = Service("/home/dailySnip/chromedriver")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get("https://vps.driverweb.com/conequip-reviews.htm")

# Waits for the Page to load fully and then takes a screenshot.
time.sleep(3)
driver.save_screenshot("staticReview.png")
driver.quit()

# x, y, w, and h are all measure in px.  x - x loc to start cropping, y - y loc to start cropping
# w - width in px, h - height in px.
x = 800
y = 0
w = 320
h = 200
width = x + w
height = y + h

# opens the image and crops it to desired size.
im = Image.open('staticReview.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('staticReview.png')
