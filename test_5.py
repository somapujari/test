from  selenium import webdriver 
driver = webdriver.Chrome() 
driver.get('https://www.google.com') 
driver.implicitly_wait(10) 
driver.quit()