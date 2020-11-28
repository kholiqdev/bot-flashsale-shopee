from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time,perf_counter
from setting import *
from datetime import datetime

browser = webdriver.Chrome(executable_path=r'./chromedriver')
browser.get("http://google.com")
