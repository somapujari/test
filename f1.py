from selenium import webdriver 
driver = webdriver.Chrome()
driver.get('https://www.facebook.com') 
driver.find_element(By.ID, 'username' ) .send_keys('soma' ) 
driver.find_element(By.ID, 'pass' ).send_keys('1234') 
driver.find_element(By.ID, 'button') .click()
assert driver.title == 'Facebook sign up  or Login' , 'login not happen '
print('end the program ' ) 
