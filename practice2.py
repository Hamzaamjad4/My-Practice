from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
import json
import time

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
  #  driver.find_element_by_xpath(
  #           "//span[contains(concat(' ', @class, ' '), ' coreSpriteInputRefresh ')]/parent::button")
   
   driver.find_element_by_xpath("//input[@name='password']").send_keys(d['password'])
   driver.find_element_by_xpath("//button[text()='Sign up']").click()
time.sleep(8)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
time.sleep(3)






