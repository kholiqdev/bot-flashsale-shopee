from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from setting import *
import time

browser = webdriver.Firefox()
browser.get(PRODUCT_URL)
browser.add_cookie({'name': 'SPC_EC', 'value': TOKEN})
browser.refresh()
sleep(5)
cart = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "btn.btn-solid-primary.btn--l.YtgjXY")))
cart.click()
print("Berhasil Add Cart")
# sleep(4)
checkout = WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.CLASS_NAME, "shopee-button-solid.shopee-button-solid--primary")))
actionChains = ActionChains(browser)
actionChains.double_click(checkout).perform()
print("Berhasil Checkout")
# WebDriverWait(browser, 60).until(ec.visibility_of_element_located((By.CLASS_NAME, "stardust-button.stardust-button--primary.stardust-button--large._22Ktrb")))
# browser.find_element_by_class_name("stardust-button.stardust-button--primary.stardust-button--large._22Ktrb").click()
sleep(4)
# order = browser.find_element_by_class_name("stardust-button.stardust-button--primary.stardust-button--large._22Ktrb")
payment = browser.find_elements_by_xpath('//div[@class="checkout-payment-setting__payment-methods-tab"]/span/button')
payment[7].click()
order = WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.CLASS_NAME, "stardust-button.stardust-button--primary.stardust-button--large._22Ktrb")))
order.send_keys(Keys.ENTER)
print("Order")
sleep(5)
# total = browser.find_element_by_class_name("_28YfJV")
# bank = browser.find_element_by_class_name("_13ScMb")
# rekening = browser.find_element_by_class_name("_1wzUBi")
# print("Detail Info")
# print("Total = "+total.text)
# print("Bank = "+bank.text)
# print("Rekening = "+rekening.text)

