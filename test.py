from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

###Closes the current tab
#driver.close()
###Closes the whole browser
#driver.quit()
###Output the title of the page
#print(driver.title)

#Keeps window open for 10s
time.sleep(10)
