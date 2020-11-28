from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep,time,perf_counter
from setting import *
from datetime import datetime

now = datetime.now()

global stop
global browser
global url_product

start_time = str(now.strftime("%H:%M:%S"))

print("Start Time =", start_time)

def __init__():
    global url_product
    url_product = input("Masukkan URL Produk : ")
    jam = input("Masukkan jam flashsale (05:00:00) : ")
    global stop
    stop = datetime.strptime(jam, '%H:%M:%S')
    if url_product == "":
        url_product = PRODUCT_URL
    add_cart()
    checkout()

def set_browser_options():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("headless")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    return option

def add_cart():
    option = set_browser_options()
    global browser
    browser = webdriver.Firefox()
    browser.get(url_product)
    browser.add_cookie({'name': 'SPC_EC', 'value': TOKEN})
    browser.refresh()
    sleep(5)
    cart = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "btn.btn-solid-primary.btn--l.YtgjXY")))
    cart.click()
    print("Menambahkan ke Keranjang")

def checkout():
    global stop
    global browser
    while True:
        now = datetime.now()
        difference = stop - datetime.strptime(now.strftime("%H:%M:%S"),"%H:%M:%S")
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            t1_start = perf_counter()
            checkout = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "shopee-button-solid.shopee-button-solid--primary")))
            actionChains = ActionChains(browser)
            actionChains.double_click(checkout).perform()
            print("Berhasil Checkout")
            sleep(2)
            WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.XPATH, '//div[@class="checkout-payment-setting__payment-methods-tab"]/span/button')))
            payment = browser.find_elements_by_xpath('//div[@class="checkout-payment-setting__payment-methods-tab"]/span/button')
            payment[2].click()
            WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.XPATH, '//div[@class="checkout-bank-transfer-item"]/div[@class="stardust-radio"]')))
            banks = browser.find_elements_by_xpath('//div[@class="checkout-bank-transfer-item"]/div[@class="stardust-radio"]')
            banks[2].click()
            order = WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.CLASS_NAME, "stardust-button.stardust-button--primary.stardust-button--large._22Ktrb")))
            order.send_keys(Keys.ENTER)
            t1_stop = perf_counter()
            print("Order")
            print("Response time in seconds : ", t1_stop-t1_start)
            print("Good bye!")
            break
        print('Time remaining: '
              + str(count_hours) + " hour(s) "
              + str(count_minutes) + " minute(s) "
              + str(count_seconds) + " second(s) "
              )
        sleep(1)

__init__()