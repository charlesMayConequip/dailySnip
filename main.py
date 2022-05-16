from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from PIL import Image
from selenium.webdriver.chrome.options import Options
from ftplib import FTP
from otherVars import *

print("the script is running")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# opening the url fullscreen in chrome, having the proper chrome driver is important
s = Service(driver_path)
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()
driver.get("https://vps.driverweb.com/conequip-reviews.htm")

# Waits for the Page to load fully and then takes a screenshot.
time.sleep(3)
driver.save_screenshot("staticReview.png")
driver.quit()

# x, y, w, and h are all measure in px.  x - x loc to start cropping, y - y loc to start cropping
# w - width in px, h - height in px.
x = 280
y = 0
w = 240
h = 135
width = x + w
height = y + h

# opens the image and crops it to desired size.
im = Image.open('staticReview.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('staticReview.png')

# transfers files with ftp
with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

# Uploading a file with ftp, first txt var is what its originally saved as, second is name it will be saved as
    with open('staticReview.png', 'rb') as f:
        ftp.storbinary('STOR ' + 'google-reviews.png', f)

    ftp.quit()
