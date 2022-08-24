from os import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Firefox()

###LOGIN INTO THE URL###

url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
time.sleep(3)
username=driver.find_element(by=By.XPATH,value="//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
password=driver.find_element(by=By.NAME,value='password').send_keys("admin123")
submit=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

###CREATING A NEW USER###

admin=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
add_button=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
time.sleep(3)
input=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("paul collings")
name=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Jhansi")
p1=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Paytabs@123")
p2=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Paytabs@123")
time.sleep(3)
element=driver.find_element(by=By.XPATH,value="//*[@class='oxd-select-text-input']")
drp=Select(element)
drp.select_by_visible_text('Admin')
p=driver.find_element(by=By.XPATH,value="//*[@class='oxd-select-text-input']")
drp=Select(p)
drp.select_by_visible_text('Enabled')
save=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click()

###LOG IN WITH CREATED USER###

username=driver.find_element(by=By.XPATH,value="//input[@class='oxd-input oxd-input--active']").send_keys("Jhansi")
password=driver.find_element(by=By.NAME,value='password').send_keys("Paytabs@123")
submit=driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
