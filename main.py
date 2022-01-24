from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from PIL import Image

# opening the url fullscreen in chrome, having the proper chrome driver is important
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
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