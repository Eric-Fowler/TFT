import numpy as np
import time
import threading
import webbrowser
import pynput
from pynput.mouse import Button, Controller
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


PATH = "D:\Programming\Web Drivers\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 1}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(PATH,options=chrome_options)


driver.get("https://www.chess.com/play/online")
time.sleep(5)
searchBtn = driver.find_element(By.LINK_TEXT, "Play")


#try:
#main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.link)))

#search = driver.find_elements_by_link_text()("Play").click()