from selenium import webdriver
import requests
from selenium .webdriver.common.by import By
from bs4 import BeautifulSoup
import json
driver=webdriver.Firefox()
url="https://reqres.in/"
driver.get(url)
response=requests.get(url)
print(response.status_code)
user=driver.find_element (by=By.XPATH,value="/html/body/div[2]/div/div/section[1]/div[1]/ul/li[1]/a").click()
page=driver.find_element (by=By.XPATH,value="/html/body/div[2]/div/div/section[1]/div[2]/div[1]/p/strong/a/span").click()
driver.switch_to.new_window('tab')
driver.get(url)

###FETCHING THE EMPLOYEE'S DETAILS###

page1=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/section[1]/div[1]/ul/li[4]/a").click()
page=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/section[1]/div[2]/div[1]/p/strong/a/span").click()
req=requests.get("https://reqres.in/api/unknown")
response=req.json()
print(response)
print("#######################################")
req=requests.get("https://reqres.in/api/users?page=2")
response=req.json()
print(response)

###CREATING  AND UPDATE THE EMPLOYEE DETAILS###
url="https://reqres.in/"
driver.switch_to.new_window('window')
driver.get(url)
create=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/section[1]/div[1]/ul/li[7]/a").click()
driver.switch_to.new_window('tab')
driver.get(url)
update=driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/section[1]/div[1]/ul/li[8]/a").click()


