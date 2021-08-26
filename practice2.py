from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
import json

#browser open

options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\repos\practice\My-Practice\chromedriver.exe")
driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')

with open('C:/repos/practice/My-Practice/data.json') as f:
  data = json.load(f)
for d in data:
   WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='emailOrPhone']"))).send_keys(d['emailOrPhone'])
   driver.find_element_by_xpath("//input[@name='fullName']").send_keys(d['fullName'])
   driver.find_element_by_xpath("//input[@name='username']").send_keys(d['username'])
   explore=driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF    ']")
   explore.click()
   driver.find_element_by_xpath("//input[@name='password']").send_keys(d['password'])

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))






