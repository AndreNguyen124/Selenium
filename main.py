import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Need to install chromedriver
driver = webdriver.Chrome('C:/Users/andre.nguyen/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('http://codepad.org/')

# Open inspector and right click the html element and select copy XPath to get the link
driver.find_element(By.XPATH, '//*[@id="editor-form"]/table/tbody/tr[2]/td[1]/nobr[10]/label/input').click()

try:
    textScreen = driver.find_element(By.XPATH, '//*[@id="textarea"]')
    textScreen.send_keys(Keys.TAB)
    textScreen.clear()
    textScreen.send_keys("print(\"Hello World\")")
except selenium.common.exceptions.NoSuchElementException:
    print("Error")
    driver.close()


driver.find_element(By.XPATH, '//*[@id="editor-form"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/button').click()

