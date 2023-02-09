from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=options)
driver.get("https://google.com")

###Keeps window open for 10s
time.sleep(1)

###Closes the current tab
# driver.close()
###Closes the whole browser
# driver.quit()
###Output the title of the page
# print(driver.title)


###Searches for the searchbar (element with name="")
search = driver.find_element("name", "q")
###Types in the search bar
search.send_keys("test")
###Hits Enter
search.send_keys(Keys.RETURN)


###Makes the script wait until the "main" element is loaded
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)            #prints all the text from the main element
    articles = main.find_element("class", "BYM4Nd")
    for article in articles:
        header = article.find_element("class", "LC201b")
        print(header.text)


finally:
    driver.quit()





###Keeps window open for 10s
time.sleep(10)
