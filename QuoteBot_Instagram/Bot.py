#Please do not change the file rights
#Vvoox
import os
import sys
from datetime import date
import pyautogui

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

url = "https://www.instagram.com/bot4quotes/"
username = "bot4quotes"
password = "067036987-Khalil"
# Message = "Your message"
# print("Sending...to "+username)
chrome_options = Options()
chrome_options.add_argument("user-data-dir=./User_Data")
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# display = Display(visible=0 , size=(800, 800))
# display.start()
webdriver1= webdriver.Chrome(options=chrome_options)
webdriver1.set_window_position(0, 0)
webdriver1.set_window_size(0, 0)
# webdriver1.driver.minimize_window()
webdriver1.get(url)
print("Open the url is done ...")
image_path = os.path.abspath('/home/vvoox/Pictures/Instargrambot/2.png')

sleep(5)

# def send_message():
#
#     webdriver1.find_element_by_xpath("//div[contains(@class, '_3FRCZ copyable-text selectable-text')]") \
#         .send_keys(username)
#     sleep(1)
#     webdriver1.find_element_by_xpath("//div[contains(@class, '_3FRCZ copyable-text selectable-text')]") \
#             .send_keys(Keys.ENTER)
#
#     webdriver1.find_element_by_xpath("//div[contains(@class, '_2FVVk _2UL8j')]") \
#             .send_keys(Message)
#     sleep(1)
#     # webdriver1.find_element_by_xpath("//input[contains(@class, '_2FVVk _2UL8j')]") \
#     #         .send_keys(Keys.ENTER)
#     webdriver1.find_element_by_xpath("//button[contains(@class, '_1U1xa')]") \
#         .send_keys(Keys.ENTER)
#     sleep(10)
#     print("Your message was sent")
#     webdriver1.quit()
#
# send_message()


def login():
    print("Connecting")
    webdriver1.find_element_by_id('loginForm')
    sleep(2)
    webdriver1.find_element_by_name('username').send_keys(username)
    webdriver1.find_element_by_name('password').send_keys(password)
    # webdriver1.find_element_by_name('continue')

    # sleep(2)
    # webdriver1.find_element_by_xpath("//input[contains(@class, '_9nyy2')]") \
    #     .send_keys(password)
    # webdriver1.send_keys(password)

    sleep(2)
    webdriver1.find_element_by_xpath("//button[contains(@class, 'sqdOP  L3NKy   y3zKF     ')]") \
            .send_keys(Keys.ENTER)
    sleep(2)
    webdriver1.find_element_by_xpath("//button[contains(@class, 'sqdOP  L3NKy   y3zKF     ')]") \
            .send_keys(Keys.ENTER)
    sleep(2)
    webdriver1.find_element_by_xpath("//button[contains(@class, 'aOOlW  bIiDR  ')]") \
        .send_keys(Keys.ENTER)
    print("Your logged in")
# login()

def loggedIn():
    # webdriver1.find_element_by_xpath("//button[contains(@class, 'aOOlW  bIiDR  ')]") \
    #     .send_keys(Keys.ENTER)
    # sleep(2)
    webdriver1.find_element_by_xpath("//a[contains(@class, 'gmFkV')]") \
        .send_keys(Keys.ENTER)

def postImage():
    webdriver1.find_element_by_xpath("//button[contains(@class, 'ext_upload_icon')]") \
        .send_keys(Keys.ENTER)
    webdriver1.find_element_by_xpath("//button[contains(@class, 'upload_to_profile_btn')]") \
        .send_keys(Keys.ENTER)
    # webdriver1.find_element_by_id("ext_upload_input").send_keys(os.getcwd()+'/home/vvoox/Pictures/quotes-about-change-5-1580500676.jpg')
    pyautogui.write('/home/vvoox/Pictures/Instargrambot/2.png')
    print("Selecting image...")
    pyautogui.press('enter')
    print("image selected")

    sleep(2)
    #set full screen of the image
    webdriver1.find_element_by_xpath("//div[contains(@class, 'expand_btn')]") \
        .click()
    print("Resizing image...")

    sleep(1)
    #Click on next to upload it
    webdriver1.find_element_by_xpath("//button[contains(@class, 'next')]") \
        .send_keys(Keys.ENTER)
    print("Resized and confirm post image")
    sleep(10)
    # Set message or tag someone
    webdriver1.find_element_by_xpath("//button[contains(@class, 'next')]") \
        .send_keys(Keys.ENTER)
    print("Image was posted")

def storyImage():
    webdriver1.find_element_by_xpath("//button[contains(@class, 'ext_upload_icon')]") \
        .send_keys(Keys.ENTER)
    webdriver1.find_element_by_xpath("//button[contains(@class, 'upload_to_stories_btn')]") \
        .send_keys(Keys.ENTER)
    # webdriver1.find_element_by_id("ext_upload_input").send_keys(os.getcwd()+'/home/vvoox/Pictures/quotes-about-change-5-1580500676.jpg')
    pyautogui.write('/home/vvoox/Pictures/Instargrambot/1.jpg')
    print("Selecting image...")
    pyautogui.press('enter')
    print("image selected")
    sleep(2)
    #Click on next to upload it
    webdriver1.find_element_by_xpath("//button[contains(@class, 'next')]") \
        .send_keys(Keys.ENTER)
    print("Resized and confirm post image")
    sleep(5)
    webdriver1.refresh()
    print("Image was posted in story")
# loggedIn()
# sleep(2)
# postImage()
storyImage()