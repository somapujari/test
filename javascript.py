import time

# from  selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
#
# element = driver.find_element(By.ID, 'name').send_keys('ssoma')
# # element = driver.find_element(By.ID, 'male')
# # driver.execute_script('window.scrollBy(0,1000)','')
# # driver.execute_script('arguments[0].scrollIntoView()',element)
# # driver.execute_script('window.scrollBy(0,document.body.scrollHeight)','')
# # driver.execute_script('arguments[0].click()',element)
# # driver.execute_script('arguments[0].style.border = "2px solid red"',element)
#
# # driver.execute_script('arguments[0].focus()', element)
# driver.execute_script('history.go(0)')  # refresh the page
#
# time.sleep(5)
#

import pytest


class Test_sample:

    @pytest.mark.skip
    def test_1(self):
        a = 20
        b = 10 + 10
        assert a == b

    def test_2(self):
        c = 20
        d = 10 * 2
        assert c == d

    def test_login(self):
        e = 'somaning'
        d = 'hi somaning  how r  u doing '
        assert e in d

    def test_login1(self):
        f = 'soma'
        g = 'soma'
        assert f == g

    def test_login2(self):
        a = 10
        b = 20
        assert a == b
