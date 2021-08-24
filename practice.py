from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#browser open
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\repos\practice\My-Practice\chromedriver.exe")
driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')

# Phone Number or Email
while True:
      Email = input("Enter your Email: ")
      if "@"and "." in Email:
         print("\n")
         break
      else:
         print("your email is incorrect") 
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='emailOrPhone']"))).send_keys(Email)

# Full Name

FullName = input("Enter your name :")
driver.find_element_by_xpath("//input[@name='fullName']").send_keys(FullName)

#User Name

UserName = input("Enter your User Name: ")
r = '{}'.format(random.randint(0, 10000))
print(UserName,r)
driver.find_element_by_xpath("//input[@name='username']").send_keys(UserName)
explore=driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()

pasword = input("Enter your pasword: ")
driver.find_element_by_xpath("//input[@name='password']").send_keys(pasword)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign up']")))






